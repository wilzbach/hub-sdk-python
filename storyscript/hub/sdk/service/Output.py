# from storyscript.hub.sdk.service.Action import Action
from storyscript.hub.sdk.service.OutputAction import OutputAction
from storyscript.hub.sdk.service.OutputProperty import OutputProperty
from storyscript.hub.sdk.service.ServiceObject import ServiceObject


# todo needs enhancements

class Output(ServiceObject):
    """
    An individual service event output with its arguments.
    """

    def __init__(self, type_, actions, properties, content_type, data):
        super().__init__(data=data)

        self._type = type_
        self._actions = actions
        self._properties = properties
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

        properties = {}
        if 'properties' in output:
            for property_name, output_property in output['properties'].items():
                properties[property_name] = OutputProperty.from_dict(data={
                    "name": property_name,
                    "output_property": output_property
                })

        return cls(
            type_=output["type"],
            actions=actions,
            properties=properties,
            content_type=output.get(
                "contentType", None
            ),
            data=data
        )

    def type(self):
        return self._type

    def content_type(self):
        return self._content_type

    def actions(self):
        return list(self._actions.values())

    def action(self, name):
        return self._actions.get(name, None)

    def properties(self):
        return list(self._properties.values())

    def property(self, name):
        return self._properties.get(name, None)
