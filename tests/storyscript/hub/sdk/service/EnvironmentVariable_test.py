import json

from storyscript.hub.sdk.service.EnvironmentVariable import EnvironmentVariable
from tests.storyscript.hub.sdk.JsonFixtureHelper import JsonFixtureHelper

env_fixture = JsonFixtureHelper.load_fixture("env_fixture")

env_fixture_json = json.dumps(env_fixture)


def test_deserialization(mocker):

    mocker.patch.object(json, 'loads', return_value=env_fixture)

    assert EnvironmentVariable.from_json(jsonstr=env_fixture_json) is not None

    json.loads.assert_called_with(env_fixture_json)


def test_serialization(mocker):

    mocker.patch.object(json, 'dumps', return_value=env_fixture_json)

    service_command = EnvironmentVariable.from_dict(data=env_fixture)

    assert service_command.as_json(compact=True) is not None
    json.dumps.assert_called_with(env_fixture, sort_keys=True)

    assert service_command.as_json() is not None
    json.dumps.assert_called_with(env_fixture, indent=4, sort_keys=True)

