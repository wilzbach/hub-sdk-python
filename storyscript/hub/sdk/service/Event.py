from storyscript.hub.sdk.service.Argument import Argument
# from storyscript.hub.sdk.service.EventOutput import EventOutput
from storyscript.hub.sdk.service.EventOutput import EventOutput
from storyscript.hub.sdk.service.HttpOptions import HttpOptions
from storyscript.hub.sdk.service.ServiceObject import ServiceObject


# todo needs enhancements

class Event(ServiceObject):
    """
    An individual service event with its arguments.
    """

    def __init__(self, name, help_, args, event_output, http_options, data):
        super().__init__(data=data)

        self._name = name
        self._help = help_
        self._args = args
        self._output = event_output
        self._http_options = http_options

    @classmethod
    def from_dict(cls, data):
        name = data["name"]
        event = data["event"]

        args = {}
        if 'arguments' in event:
            for arg_name, arg in event['arguments'].items():
                args[arg_name] = Argument.from_dict(data={
                    "name": arg_name,
                    "argument": arg
                })

        event_output = None
        if 'output' in event:
            event_output = EventOutput.from_dict(data={
                "event_output": event["output"]
            })

        http_options = event.get(
            'http', None
        )

        if http_options is not None:
            http_options = HttpOptions.from_dict(data={
                "http_options": http_options
            })

        help_ = event.get(
            'help', 'No help_ available'
        )

        return cls(
            name=name,
            help_=help_,
            args=args,
            event_output=event_output,
            http_options=http_options,
            data=data
        )

    def name(self):
        return self._name

    def help(self):
        return self._help

    def output(self):
        return self._output

    def args(self):
        return list(self._args.values())

    def arg(self, name):
        return self._args.get(name, None)
