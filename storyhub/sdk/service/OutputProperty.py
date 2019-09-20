from storyhub.sdk.service.ServiceObject import ServiceObject


class OutputProperty(ServiceObject):
    """
    A service output Property.
    """

    def __init__(self, name, type_, help_, data):
        super().__init__(data=data)

        self._name = name
        self._help = help_
        self._type = type_

    @classmethod
    def from_dict(cls, data):
        name = data["name"]
        output_property = data["output_property"]

        return cls(
            name=name,
            type_=output_property["type"],
            help_=output_property.get(
                'help', 'No help available.'
            ),
            data=data
        )

    def name(self):
        return self._name

    def help(self):
        return self._help

    def type(self):
        return self._type
