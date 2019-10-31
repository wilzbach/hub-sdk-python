from storyhub.sdk.service.output.OutputAny import OutputAny
from storyhub.sdk.service.output.OutputBase import OutputBase
from storyhub.sdk.service.output.OutputUtils import OutputUtils


class OutputList(OutputBase):
    """
    A service output list.
    """

    def __init__(self, elements, **kwargs):
        super().__init__(**kwargs)

        self._elements = elements

    @classmethod
    def from_dict(cls, data):
        kwargs = OutputBase.parse_dict(data)

        if 'list' in data and 'elements' in data['list']:
            kwargs['elements'] = OutputUtils.parse_type(
                data['list']['elements']
            )
        else:
            kwargs['elements'] = OutputAny.create()

        return cls(**kwargs)

    def elements(self):
        return self._elements
