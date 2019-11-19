from storyhub.sdk.service.Argument import Argument
from storyhub.sdk.service.ServiceObject import ServiceObject


class Entrypoint(ServiceObject):
    """
    This represents an entrypoint configuration for a service.
    """

    def __init__(self, help_, args, data):
        super().__init__(data)

        self._help = help_
        self._args = args

    @classmethod
    def from_dict(cls, data):
        entrypoint = data["entrypoint"]

        args = {}
        if "arguments" in entrypoint:
            for arg_name, arg in entrypoint["arguments"].items():
                args[arg_name] = Argument.from_dict(
                    data={"name": arg_name, "argument": arg}
                )

        return cls(
            help_=entrypoint.get("help", "No help available."),
            args=args,
            data=data,
        )

    def help(self):
        return self._help

    def args(self):
        return list(self._args.values())

    def arg(self, name):
        return self._args.get(name, None)
