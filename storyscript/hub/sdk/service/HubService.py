from storyscript.hub.sdk.service.Configuration import Configuration
from storyscript.hub.sdk.service.ServiceObject import ServiceObject


class HubService(ServiceObject):
    """
    An individual service
    """

    def __init__(self, name, alias, owner, uuid, state, certified, public, topics, description, readme, configuration, data):
        super().__init__(data)

        self._name = name
        self._alias = alias
        self._owner = owner
        self._uuid = uuid
        self._state = state
        self._certified = certified
        self._public = public
        self._topics = topics
        self._description = description
        self._readme = readme
        self._configuration = configuration

    @classmethod
    def from_dict(cls, data):
        service = data["hub_service"]

        service_data = service["service"]
        return cls(
            name=service_data['name'],
            alias=service_data['alias'],
            owner=service_data['owner']['username'],
            state=service["state"],
            uuid=service["serviceUuid"],
            certified=service_data["isCertified"],
            public=service_data["public"],
            topics=service_data["topics"],
            description=service_data['description'],
            readme=service_data.get(
                'readme', 'No readme found.'
            ),
            data=data,
            configuration=Configuration.from_dict(data={
                "configuration": service["configuration"]
            })
        )

    def name(self):
        return self._name

    def alias(self):
        return self._alias

    def owner(self):
        return self._owner

    def description(self):
        return self._description

    def state(self):
        return self._state

    def certified(self):
        return self._certified

    def public(self):
        return self._public

    def readme(self):
        return self._readme

    def configuration(self):
        return self._configuration
