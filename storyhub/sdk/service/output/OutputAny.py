from storyhub.sdk.service.output.OutputBase import OutputBase


class OutputAny(OutputBase):
    """
    A service output any type.
    """

    @classmethod
    def create(cls):
        kwargs = {
            'data': {},
        }
        return cls(**kwargs)
