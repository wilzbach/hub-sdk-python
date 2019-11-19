from storyhub.sdk.service.ServiceObject import ServiceObject


class Volume(ServiceObject):
    """
    A service volume.
    """

    def __init__(self, name, target, data):
        super().__init__(data=data)

        self._name = name
        self._target = target

    @classmethod
    def from_dict(cls, data):
        name = data["name"]
        volume = data["volume"]

        return cls(name=name, target=volume["target"], data=data)

    def name(self):
        return self._name

    def target(self):
        return self._target
