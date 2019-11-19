import json

from storyhub.sdk.service.Argument import Argument
from storyhub.sdk.service.Command import Command
from tests.storyhub.sdk.JsonFixtureHelper import JsonFixtureHelper

command_fixture = JsonFixtureHelper.load_fixture("command_fixture")

command_fixture_json = json.dumps(command_fixture)


def test_deserialization(mocker):

    mocker.patch.object(json, "loads", return_value=command_fixture)

    mocker.patch.object(Argument, "from_dict")

    assert Command.from_json(jsonstr=command_fixture_json) is not None

    json.loads.assert_called_with(command_fixture_json)

    Argument.from_dict.assert_called_with(
        data={
            "name": "path",
            "argument": command_fixture["command"]["arguments"]["path"],
        }
    )


def test_serialization(mocker):

    mocker.patch.object(json, "dumps", return_value=command_fixture_json)

    service_command = Command.from_dict(data=command_fixture)

    assert service_command.as_json(compact=True) is not None
    json.dumps.assert_called_with(command_fixture, sort_keys=True)

    assert service_command.as_json() is not None
    json.dumps.assert_called_with(command_fixture, indent=4, sort_keys=True)
