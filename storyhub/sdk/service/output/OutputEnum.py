from storyhub.sdk.service.output.OutputBase import OutputBase


class OutputEnum(OutputBase):
    """
    A service output enum.
    """

    def __init__(self, enum=None, **kwargs):
        super().__init__(**kwargs)

        self._enum = enum

    @classmethod
    def from_dict(cls, data):
        kwargs = OutputBase.parse_dict(data)

        if "enum" in data:
            kwargs["enum"] = data["enum"]

        return cls(**kwargs)

    def enum(self):
        return self._enum
