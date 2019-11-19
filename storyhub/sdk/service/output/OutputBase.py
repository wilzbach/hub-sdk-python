from storyhub.sdk.service.ServiceObject import ServiceObject


class OutputBase(ServiceObject):
    """
    Base of all service output types.
    """

    def __init__(self, data, help_=None, name=None):
        super().__init__(data=data)

        self._help = help_
        self._name = name

    @classmethod
    def from_dict(cls, data):
        kwargs = OutputBase.parse_dict(data)
        return cls(**kwargs)

    @classmethod
    def parse_dict(cls, data):
        return {
            "help_": data.get("help", None),
            "name": data.get("name", None),
            "data": data,
        }

    def name(self):
        return self._name

    def help(self):
        if self._help is None:
            return "No help available"
        return self._help
