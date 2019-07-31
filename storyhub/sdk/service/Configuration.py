from storyhub.sdk.service.Action import Action
from storyhub.sdk.service.Command import Command
from storyhub.sdk.service.Entrypoint import Entrypoint
from storyhub.sdk.service.EnvironmentVariable import EnvironmentVariable
from storyhub.sdk.service.Lifecycle import Lifecycle
from storyhub.sdk.service.ServiceInfo import ServiceInfo
from storyhub.sdk.service.ServiceObject import ServiceObject
from storyhub.sdk.service.Volume import Volume


class Configuration(ServiceObject):
    """
    Represents a service configuration
    """

    def __init__(self, actions, commands, volumes, entrypoint, service_info, environment_variables, lifecycle, data):
        super().__init__(data)

        self._actions = actions
        self._commands = commands
        self._volumes = volumes
        self._entrypoint = entrypoint
        self._info = service_info
        self._environment_variables = environment_variables
        self._lifecycle = lifecycle


    @classmethod
    def from_dict(cls, data):
        configuration = data["configuration"]

        entrypoint = None
        if 'entrypoint' in configuration:
            entrypoint = Entrypoint.from_dict(data={
                "entrypoint": configuration['entrypoint']
            })

        lifecycle = None
        if 'lifecycle' in configuration:
            lifecycle = Lifecycle.from_dict(data={
                "lifecycle": configuration['lifecycle']
            })

        service_info = None
        if 'info' in configuration:
            service_info = ServiceInfo.from_dict(data={
                "service_info": configuration['info']
            })

        volumes = {}
        if 'volumes' in configuration:
            for name, volume in configuration['volumes'].items():
                volumes[name] = Volume.from_dict(data={
                    "name": name,
                    "volume": volume
                })

        actions = {}
        if 'actions' in configuration:
            for name, action in configuration['actions'].items():
                actions[name] = Action.from_dict(data={
                    "name": name,
                    "action": action
                })

        commands = {}
        if 'commands' in configuration:
            for name, command in configuration['commands'].items():
                commands[name] = Command.from_dict(data={
                    "name": name,
                    "command": command
                })

        environment_variables = {}
        if 'environment' in configuration:
            for name, environment_variable in configuration['environment'].items():
                environment_variables[name] = EnvironmentVariable.from_dict(data={
                    "name": name,
                    "environment_variable": environment_variable
                })

        return cls(
            actions=actions,
            commands=commands,
            entrypoint=entrypoint,
            volumes=volumes,
            service_info=service_info,
            environment_variables=environment_variables,
            lifecycle=lifecycle,
            data=data
        )

    def actions(self):
        return list(self._actions.values())

    def action(self, action):
        return self._actions.get(action, None)

    def commands(self):
        return list(self._commands.values())

    def command(self, command):
        return self._commands.get(command, None)

    def volumes(self):
        return list(self._volumes.values())

    def volume(self, volume):
        return self._volumes.get(volume, None)

    def environment_variables(self):
        return list(self._environment_variables.values())

    def environment_variable(self, variable):
        return self._environment_variables.get(variable, None)

    def entrypoint(self):
        return self._entrypoint

    def lifecycle(self):
        return self._lifecycle

    def info(self):
        return self._info
