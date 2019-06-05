# -*- coding: utf-8 -*-
import json
import os
import sys
from threading import Lock

from storyscript.hub.sdk.AutoUpdateThread import AutoUpdateThread
from storyscript.hub.sdk.GraphQL import GraphQL
from storyscript.hub.sdk.db.Database import Database
from storyscript.hub.sdk.db.Service import Service

from cachetools import TTLCache, cached

from peewee import DoesNotExist


class StoryscriptHub:
    update_thread = None

    retry_lock = Lock()
    update_lock = Lock()

    ttl_cache_for_services = TTLCache(maxsize=128, ttl=1 * 60)
    ttl_cache_for_service_names = TTLCache(maxsize=1, ttl=1 * 60)

    @staticmethod
    def get_config_dir(app):
        if sys.platform == 'win32':
            p = os.getenv('APPDATA')
        else:
            p = os.getenv('XDG_DATA_HOME', os.path.expanduser('~/'))

        return os.path.join(p, app)

    def __init__(self, db_path: str = None, auto_update: bool = True):
        if db_path is None:
            db_path = StoryscriptHub.get_config_dir('.storyscript')

        os.makedirs(db_path, exist_ok=True)

        self.db_path = db_path

        if auto_update:
            self.update_thread = AutoUpdateThread(
                update_function=self.update_cache)

    @cached(cache=ttl_cache_for_service_names)
    def get_all_service_names(self) -> [str]:
        """
        Get all service names and aliases from the database.

        :return: An array of strings, which might look like:
        ["hello", "universe/hello"]
        """
        services = []
        with Database(self.db_path):
            for s in Service.select(Service.name, Service.alias,
                                    Service.username):
                if s.alias:
                    services.append(s.alias)

                services.append(f'{s.username}/{s.name}')

        return services

    @cached(cache=ttl_cache_for_services)
    def get(self, alias=None, owner=None, name=None) -> Service:
        """
        Get a service from the database.

        :param alias: Takes precedence when specified over owner/name
        :param owner: The owner of the service
        :param name: The name of the service
        :return: Returns a Service instance, with all fields populated
        """
        service = self._get(alias, owner, name)

        if service is None:
            # Maybe it's new in the Hub?
            with self.retry_lock:
                service = self._get(alias, owner, name)
                if service is None:
                    self.update_cache()
                    service = self._get(alias, owner, name)

        if service is not None:
            # We store JSON as plain text because some Python installations
            # do not have support for the json1 extension.
            # First encountered on CircleCI.
            if isinstance(service, Service):
                if service.topics is not None:
                    service.topics = json.loads(service.topics)

                if service.configuration is not None:
                    service.configuration = json.loads(service.configuration)

        return service

    def _get(self, alias: str = None, owner: str = None, name: str = None):
        try:
            if alias is not None and alias.count("/") == 1:
                owner, name = alias.split('/')
                alias = None

            with Database(self.db_path):
                if alias:
                    service = Service.select().where(Service.alias == alias)
                else:
                    service = Service.select().where(
                        (Service.username == owner) & (Service.name == name))

                return service.get()
        except DoesNotExist:
            return None

    def update_cache(self):
        services = GraphQL.get_all()

        with Database(self.db_path) as db:
            with db.atomic(lock_type='IMMEDIATE'):
                Service.delete().execute()
                for service in services:
                    Service.create(
                        service_uuid=service['serviceUuid'],
                        name=service['service']['name'],
                        alias=service['service']['alias'],
                        username=service['service']['owner']['username'],
                        description=service['service']['description'],
                        certified=service['service']['isCertified'],
                        public=service['service']['public'],
                        topics=json.dumps(service['service']['topics']),
                        state=service['state'],
                        configuration=json.dumps(service['configuration']),
                        readme=service['readme'],
                        raw_data=json.dumps(service))

        with self.update_lock:
            self.ttl_cache_for_service_names.clear()
            self.ttl_cache_for_services.clear()

        return True
