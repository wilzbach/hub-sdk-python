# -*- coding: utf-8 -*-
from functools import lru_cache
import os
import sys

from asyncy.hub.sdk.GraphQL import GraphQL
from asyncy.hub.sdk.db.Database import Database
from asyncy.hub.sdk.db.Service import Service


class AsyncyHub:
    # TODO: add automatic retry
    # TODO: add background updates
    @staticmethod
    def get_config_dir(app):
        if sys.platform == 'win32':
            p = os.getenv('APPDATA')
        else:
            p = os.getenv('XDG_DATA_HOME', os.path.expanduser('~/'))

        return os.path.join(p, app)

    def __init__(self, db_path: str = None):
        if db_path is None:
            db_path = AsyncyHub.get_config_dir('.asyncy')

        os.makedirs(db_path, exist_ok=True)

        self.db_path = db_path

    @lru_cache(maxsize=1)
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

    @lru_cache(maxsize=28)
    def get(self, alias=None, owner=None, name=None) -> Service:
        """
        Get a service from the database.

        :param alias: Takes precedence when specified over owner/name
        :param owner: The owner of the service
        :param name: The name of the service
        :return: Returns a Service instance, with all fields populated
        """
        with Database(self.db_path):
            if alias:
                service = Service.select().where(Service.alias == alias)
            else:
                service = Service.select().where(
                    (Service.username == owner) & (Service.name == name))
        return service.get()

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
                        topics=service['service']['topics'],
                        state=service['state'],
                        configuration=service['configuration'],
                        readme=service['readme'])
        self.get.cache_clear()
        self.get_all_service_names.cache_clear()
        return True
