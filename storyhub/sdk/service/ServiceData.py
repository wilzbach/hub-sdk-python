from storyhub.sdk.service.Configuration import Configuration
from storyhub.sdk.service.Service import Service
from storyhub.sdk.service.ServiceObject import ServiceObject


class ServiceData(ServiceObject):
    """
    This represents an entire service stored within the Storyscript Hub.
    """

    def __init__(self, name, uuid, service, state, readme, configuration, data):
        super().__init__(data)

        self._name = name
        self._service = service
        self._uuid = uuid
        self._state = state
        self._readme = readme
        self._configuration = configuration

    @classmethod
    def from_dict(cls, data):
        service_data = data["service_data"]

        return cls(
            name=service_data["service"]['name'],
            service=Service.from_dict(data={
                "service": service_data["service"]
            }),
            state=service_data["state"],
            uuid=service_data["serviceUuid"],
            readme=service_data.get(
                'readme', 'No readme found.'
            ),
            configuration=Configuration.from_dict(data={
                "configuration": service_data["configuration"]
            }),
            data=data
        )

    def name(self):
        """
        This acts as a helper for easily accessing the name of the service. For example the value stored
         within {"service":{"name":"helloworld"}}

        :return: service name
        """
        return self._name

    def uuid(self):
        return self._uuid

    def service(self):
        return self._service

    def readme(self):
        return self._readme

    def state(self):
        return self._state

    def configuration(self):
        return self._configuration
