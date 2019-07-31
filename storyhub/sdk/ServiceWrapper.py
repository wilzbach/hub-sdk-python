import json
from uuid import UUID

from storyhub.sdk.GraphQL import GraphQL
from storyhub.sdk.service.ServiceData import ServiceData


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return obj.hex
        return json.JSONEncoder.default(self, obj)


class ServiceWrapper:
    """
    The ServiceWrapper provides an improved way to access storyscript
    hub services
    """
    def __init__(self, services=None):
        self.services = {}
        self.reload_services(services)

    @classmethod
    def from_dict(cls, dictionary=None):
        services = []

        if dictionary is not None:
            services = dictionary

        return cls(services)

    @classmethod
    def from_json(cls, jsonstr):
        services = []

        if jsonstr is not None:
            services = json.loads(jsonstr)

        return cls(services)

    @classmethod
    def from_json_file(cls, path):
        with open(path, 'r') as f:
            jsonstr = f.read()
            return cls.from_json(jsonstr=jsonstr)

    def reload_services(self, services):
        # reset services
        self.services = {}

        if type(services) is list:
            for service in services:
                if type(service) is dict:
                    service_data = service["service"]
                    self.services[(service_data["owner"]["username"] + '/' +
                                   service_data["name"])] = service
                else:
                    assert type(service) is str
                    # this allows us to utilize dynamic loading
                    for _service in GraphQL.get_all():
                        service_service = _service["service"]
                        service_owner = service_service["owner"]["username"]
                        service_name = service_service["name"]
                        service_alias = service_service["alias"]
                        if service == service_owner + "/" + service_name or \
                                service == service_alias:
                            self.services[service_owner + "/" + service_name] \
                                = _service

        elif type(services) is dict:
            for service in services:
                _service = services[service]
                service_owner = _service["service"]["owner"]["username"]
                service_name = _service["service"]["name"]
                self.services[service_owner + "/" + service_name] = _service

    def as_json(self):
        services = []

        for service in self.services:
            services.append(self.services[service])

        return json.dumps(services, indent=4, sort_keys=True, cls=UUIDEncoder)

    def as_json_file(self, out_file):
        if out_file is not None:
            with open(out_file, 'w') as f:
                f.write(self.as_json())

    def get_all_service_names(self, include_aliases=True):
        service_names = []

        for service in self.services:
            _service = self.services[service]["service"]
            service_names.append(service)
            alias = _service["alias"]

            if include_aliases and alias is not None \
                    and alias not in service_names:
                service_names.append(alias)

        return service_names

    def get(self, alias=None, owner=None, name=None):
        service = None

        if alias and alias in self.services:
            service = self.services[alias]
        elif f'{owner}/{name}' in self.services:
            service = self.services[f'{owner}/{name}']
        else:
            for _service in self.services:
                service_data = self.services[_service]["service"]
                if owner is not None and name is not None and\
                        service_data["owner"]["username"] == owner and \
                        service_data["name"] == name:
                    service = self.services[_service]
                elif name is not None and service_data["name"] == name:
                    service = self.services[_service]
                elif alias is not None and (service_data["alias"] == alias or
                                            service_data["name"] == alias):
                    service = self.services[_service]

        if service is None:
            return None
        else:
            return ServiceData.from_dict(data={
                "service_data": service
            })
