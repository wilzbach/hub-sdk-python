import json

from storyscript.hub.sdk.service.Argument import Argument
from storyscript.hub.sdk.service.Entrypoint import Entrypoint
from tests.storyscript.hub.sdk.JsonFixtureHelper import JsonFixtureHelper

entry_point_fixture = JsonFixtureHelper.load_fixture("entrypoint_fixture")

entry_point_fixture_json = json.dumps(entry_point_fixture)


def test_deserialization(mocker):

    mocker.patch.object(json, 'loads', return_value=entry_point_fixture)

    mocker.patch.object(Argument, 'from_dict')

    assert Entrypoint.from_json(jsonstr=entry_point_fixture_json) is not None

    json.loads.assert_called_with(entry_point_fixture_json)

    Argument.from_dict.assert_called_with(data={
        "name": "path",
        "argument": entry_point_fixture["entrypoint"]["arguments"]["path"]
    })


def test_serialization(mocker):

    mocker.patch.object(json, 'dumps', return_value=entry_point_fixture_json)

    service_entry_point = Entrypoint.from_dict(data=entry_point_fixture)

    # ensure that the compact option works
    assert service_entry_point.as_json(compact=True) is not None
    json.dumps.assert_called_with(entry_point_fixture, sort_keys=True)

    assert service_entry_point.as_json() is not None
    json.dumps.assert_called_with(entry_point_fixture, indent=4, sort_keys=True)

