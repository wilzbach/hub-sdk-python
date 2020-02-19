# -*- coding: utf-8 -*-
import json
import os
from threading import Lock
from typing import Union
from unittest.mock import MagicMock

from appdirs import user_cache_dir

from cachetools import TTLCache, cached

from peewee import DoesNotExist

from storyhub.sdk.AutoUpdateThread import AutoUpdateThread
from storyhub.sdk.GraphQL import GraphQL
from storyhub.sdk.ServiceWrapper import ServiceWrapper
from storyhub.sdk.db.Database import Database
from storyhub.sdk.db.Service import Service
from storyhub.sdk.service.ServiceData import ServiceData

# expose the ServiceWrapper as StoryscriptHub during the migration to the new
# runtime
StoryscriptHub = ServiceWrapper


class ArchivedStoryscriptHub:
    update_thread = None

    retry_lock = Lock()
    update_lock = Lock()

    ttl_cache_for_services = TTLCache(maxsize=128, ttl=1 * 60)
    ttl_cache_for_service_names = TTLCache(maxsize=1, ttl=1 * 60)

    @staticmethod
    def get_cache_dir():
        return user_cache_dir("storyscript", "hub-sdk")

    def __init__(self, db_path: str = None, auto_update: bool = True):
        """
        StoryscriptHub - a utility to access Storyscript's hub service data.

        :param db_path: The path for the database caching file
        :param auto_update: Will automatically pull services from the hub
        every 30 seconds
        """

        if db_path is None:
            db_path = StoryscriptHub.get_cache_dir()

        os.makedirs(db_path, exist_ok=True)

        self.db_path = db_path

        # We are not updating cache over here since, it makes
        # startup slow. If need arises in case of missing service
        # we will update the cache. For long running service
        # cache will be updated automatically as well via the
        # AutoUpdateThread.
        self._service_wrapper = ServiceWrapper()

        if auto_update:
            self.update_thread = AutoUpdateThread(
                update_function=self.update_cache
            )

    @cached(cache=ttl_cache_for_service_names)
    def get_all_service_names(self) -> [str]:
        """
        Get all service names and aliases from the database.

        :return: An array of strings, which might look like:
        ["hello", "universe/hello"]
        """
        services = []
        with Database(self.db_path):
            for s in Service.select(
                Service.name, Service.alias, Service.username
            ):
                if s.alias:
                    services.append(s.alias)

                services.append(f"{s.username}/{s.name}")

        return services

    @cached(cache=ttl_cache_for_services)
    def get(
        self, alias=None, owner=None, name=None
    ) -> Union[Service, ServiceData]:
        """
        Get a service from the database.

        :param alias: Takes precedence when specified over owner/name
        :param owner: The owner of the service
        :param name: The name of the service
        :return: Returns a :py:class:~.sdk.service.ServiceData.ServiceData
        object instance.
        """

        service = None

        service = self._service_wrapper.get(
            alias=alias, owner=owner, name=name
        )
        if service is not None:
            return service

        if service is None:
            service = self._get(alias, owner, name)

        if service is None:
            # Maybe it's new in the Hub?
            with self.retry_lock:
                service = self._get(alias, owner, name)
                if service is None:
                    self.update_cache()
                    service = self._get(alias, owner, name)

        if service is not None:
            # ensures test don't break
            if isinstance(service, MagicMock):
                return service

            assert isinstance(service, Service)
            # we can safely convert this object since it was probably loaded
            # from the cache
            return ServiceData.from_dict(
                data={"service_data": json.loads(service.raw_data)}
            )

        return service

    def _get(self, alias: str = None, owner: str = None, name: str = None):
        try:
            if alias is not None and alias.count("/") == 1:
                owner, name = alias.split("/")
                alias = None

            with Database(self.db_path):
                if alias:
                    service = Service.select().where(Service.alias == alias)
                else:
                    service = Service.select().where(
                        (Service.username == owner) & (Service.name == name)
                    )

                return service.get()
        except DoesNotExist:
            return None

    def update_cache(self):
        services = GraphQL.get_all()

        # tell the service wrapper to reload any services from the cache.
        if self._service_wrapper is not None:
            self._service_wrapper.reload_services(services)

        with Database(self.db_path) as db:
            with db.atomic(lock_type="IMMEDIATE"):
                Service.delete().execute()
                for service in services:
                    Service.create(
                        service_uuid=service["serviceUuid"],
                        name=service["service"]["name"],
                        alias=service["service"]["alias"],
                        username=service["service"]["owner"]["username"],
                        description=service["service"]["description"],
                        certified=service["service"]["isCertified"],
                        public=service["service"]["public"],
                        topics=json.dumps(service["service"]["topics"]),
                        state=service["state"],
                        configuration=json.dumps(service["configuration"]),
                        readme=service["readme"],
                        raw_data=json.dumps(service),
                    )

        with self.update_lock:
            self.ttl_cache_for_service_names.clear()
            self.ttl_cache_for_services.clear()

        return True
