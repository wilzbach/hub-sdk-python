import json

from storyhub.sdk.service.Argument import Argument
from tests.storyhub.sdk.JsonFixtureHelper import JsonFixtureHelper

argument_fixture = JsonFixtureHelper.load_fixture("argument_fixture")

argument_fixture_json = json.dumps(argument_fixture)


def test_deserialization(mocker):

    mocker.patch.object(json, 'loads', return_value=argument_fixture)

    assert Argument.from_json(jsonstr=argument_fixture_json) is not None

    json.loads.assert_called_with(argument_fixture_json)


def test_serialization(mocker):

    mocker.patch.object(json, 'dumps', return_value=argument_fixture_json)

    service_command = Argument.from_dict(data=argument_fixture)

    assert service_command.as_json(compact=True) is not None
    json.dumps.assert_called_with(argument_fixture, sort_keys=True)

    assert service_command.as_json() is not None
    json.dumps.assert_called_with(argument_fixture, indent=4, sort_keys=True)

