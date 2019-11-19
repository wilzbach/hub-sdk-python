from storyhub.sdk.service.output.OutputAny import OutputAny
from storyhub.sdk.service.output.OutputBase import OutputBase
from storyhub.sdk.service.output.OutputUtils import OutputUtils


class OutputMap(OutputBase):
    """
    A service output Map.
    """

    def __init__(self, keys, values, **kwargs):
        super().__init__(**kwargs)

        self._keys = keys
        self._values = values

    @classmethod
    def from_dict(cls, data):
        kwargs = OutputBase.parse_dict(data)

        if "map" in data and "keys" in data["map"]:
            kwargs["keys"] = OutputUtils.parse_type(data["map"]["keys"])
        else:
            kwargs["keys"] = OutputAny.create()

        if "map" in data and "values" in data["map"]:
            kwargs["values"] = OutputUtils.parse_type(data["map"]["values"])
        else:
            kwargs["values"] = OutputAny.create()

        return cls(**kwargs)

    def keys(self):
        return self._keys

    def values(self):
        return self._values
