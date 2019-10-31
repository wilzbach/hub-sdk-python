from storyhub.sdk.service.ServiceObject import ServiceObject
from storyhub.sdk.service.output.OutputAction import OutputAction
from storyhub.sdk.service.output.OutputUtils import OutputUtils


class ServiceOutput(ServiceObject):
    """
    An individual service event output with its arguments.
    """

    def __init__(self, type_, actions, content_type, data):
        super().__init__(data=data)

        self._type = type_
        self._actions = actions
        self._content_type = content_type

    @classmethod
    def from_dict(cls, data):
        output = data["output"]

        actions = {}
        if 'actions' in output:
            for action_name, action in output['actions'].items():
                actions[action_name] = OutputAction.from_dict(data={
                    "name": action_name,
                    "output_action": action
                })

        ty = OutputUtils.parse_type(output)

        return cls(
            type_=ty,
            actions=actions,
            content_type=output.get(
                "contentType", None
            ),
            data=data,
        )

    def type(self):
        return self._type

    def content_type(self):
        return self._content_type

    def actions(self):
        return list(self._actions.values())

    def action(self, name):
        return self._actions.get(name, None)
