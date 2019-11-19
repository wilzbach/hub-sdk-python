from storyhub.sdk.service.LifecycleOption import (
    LifecycleOption,
    LifecycleOptionType,
)
from storyhub.sdk.service.ServiceObject import ServiceObject


class Lifecycle(ServiceObject):
    def __init__(self, startup, shutdown, data):
        super().__init__(data)

        self._startup = startup
        self._shutdown = shutdown

    @classmethod
    def from_dict(cls, data):
        lifecycle = data["lifecycle"]

        startup = None

        if "startup" in lifecycle:
            startup = LifecycleOption.from_dict(
                data={
                    "type": LifecycleOptionType.STARTUP,
                    "lifecycle_option": lifecycle["startup"],
                }
            )

        shutdown = None

        if "shutdown" in lifecycle:
            shutdown = LifecycleOption.from_dict(
                data={
                    "type": LifecycleOptionType.SHUTDOWN,
                    "lifecycle_option": lifecycle["shutdown"],
                }
            )

        return cls(startup=startup, shutdown=shutdown, data=data)

    def startup(self):
        return self._startup

    def shutdown(self):
        return self._shutdown
