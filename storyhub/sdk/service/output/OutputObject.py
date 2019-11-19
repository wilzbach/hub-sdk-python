from storyhub.sdk.service.output.OutputBase import OutputBase
from storyhub.sdk.service.output.OutputUtils import OutputUtils


class OutputObject(OutputBase):
    """
    A service output object with properties.
    """

    def __init__(self, properties, **kwargs):
        super().__init__(**kwargs)

        self._properties = properties

    @classmethod
    def from_dict(cls, data):
        kwargs = OutputBase.parse_dict(data)
        if 'properties' in data:
            kwargs['properties'] = {
                k: OutputUtils.parse_type(v)
                for k, v in data['properties'].items()
            }
        else:
            kwargs['properties'] = {}

        return cls(**kwargs)

    def property(self, name):
        return self._properties.get(name, None)

    def properties(self):
        return self._properties
