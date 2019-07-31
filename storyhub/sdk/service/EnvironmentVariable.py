from storyhub.sdk.service.ServiceObject import ServiceObject


class EnvironmentVariable(ServiceObject):

    """
    This represents an environmental variable that would be stored within the configuration object
    of a service.
    """

    def __init__(self, name, help_, type_, pattern, required, default, sensitive, data):
        super().__init__(data)

        self._name = name
        self._help = help_
        self._type = type_
        self._pattern = pattern
        self._required = required
        self._default = default
        self._sensitive = sensitive

    @classmethod
    def from_dict(cls, data):
        name = data["name"]
        environment_variable = data["environment_variable"]

        return cls(
            name=name,
            help_=environment_variable.get(
                'help', 'No description available'
            ),
            type_=environment_variable["type"],
            pattern=environment_variable.get(
                'pattern', None
            ),
            required=environment_variable.get(
                'required', False
            ),
            default=environment_variable.get(
                'default', False
            ),
            sensitive=environment_variable.get(
                'sensitive', False
            ),
            data=data
        )

    def name(self):
        return self._name

    def help(self):
        return self._help

    def type(self):
        return self._type

    def required(self):
        return self._required

    def default(self):
        return self._default