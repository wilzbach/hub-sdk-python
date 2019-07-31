import json

from storyhub.sdk.service.Service import Service
from tests.storyhub.sdk.JsonFixtureHelper import JsonFixtureHelper

service_fixture = JsonFixtureHelper.load_fixture("service_fixture")

service_fixture_json = json.dumps(service_fixture)


def test_deserialization(mocker):

    mocker.patch.object(json, 'loads', return_value=service_fixture)

    assert Service.from_json(jsonstr=service_fixture_json) is not None

    json.loads.assert_called_with(service_fixture_json)


def test_serialization(mocker):

    mocker.patch.object(json, 'dumps', return_value=service_fixture_json)

    service_command = Service.from_dict(data=service_fixture)

    assert service_command.as_json(compact=True) is not None
    json.dumps.assert_called_with(service_fixture, sort_keys=True)

    assert service_command.as_json() is not None
    json.dumps.assert_called_with(service_fixture, indent=4, sort_keys=True)