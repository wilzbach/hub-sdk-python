# from storyscript.hub.sdk.service.Action import Action
from storyscript.hub.sdk.service.EventOutputAction import EventOutputAction
from storyscript.hub.sdk.service.EventOutputProperty import EventOutputProperty
from storyscript.hub.sdk.service.ServiceObject import ServiceObject


# todo needs enhancements

class EventOutput(ServiceObject):
    """
    An individual service event output with its arguments.
    """

    def __init__(self, type_, actions, properties, data):
        super().__init__(data=data)

        self._type = type_
        self._actions = actions
        self._properties = properties

    @classmethod
    def from_dict(cls, data):
        event_output = data["event_output"]

        actions = {}
        if 'actions' in event_output:
            for action_name, action in event_output['actions'].items():
                actions[action_name] = EventOutputAction.from_dict(data={
                    "name": action_name,
                    "output_action": action
                })

        properties = {}
        if 'properties' in event_output:
            for property_name, output_property in event_output['properties'].items():
                properties[property_name] = EventOutputProperty.from_dict(data={
                    "name": property_name,
                    "output_property": output_property
                })

        return cls(
            type_=event_output["type"],
            actions=actions,
            properties=properties,
            data=data
        )

    def type(self):
        return self._type

    def actions(self):
        return list(self._actions.values())

    def action(self, name):
        return self._actions.get(name, None)

    def properties(self):
        return list(self._properties.values())

    def property(self, name):
        return self._properties.get(name, None)
