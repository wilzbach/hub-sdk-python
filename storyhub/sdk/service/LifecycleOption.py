from enum import Enum

from storyhub.sdk.service.ServiceObject import ServiceObject


class LifecycleOptionType(Enum):
    STARTUP = "startup"
    SHUTDOWN = "shutdown"


class LifecycleOption(ServiceObject):

    def __init__(self, type_: LifecycleOptionType, command, timeout, data):
        super().__init__(data)

        self._type = type_
        self._command = command
        self._timeout = timeout

    @classmethod
    def from_dict(cls, data):
        lifecycle_option = data["lifecycle_option"]

        return cls(
            type_=data["type"],
            command=lifecycle_option.get(
                'command', []
            ),
            timeout=lifecycle_option.get(
                'timeout', None
            ),
            data=data
        )

    def type(self):
        return self._type

    def command(self):
        return list(self._command)

    def timeout(self):
        return self._timeout
