import json

from storyhub.sdk.service.Volume import Volume
from tests.storyhub.sdk.JsonFixtureHelper import JsonFixtureHelper

volume_fixture = JsonFixtureHelper.load_fixture("volume_fixture")

volume_fixture_json = json.dumps(volume_fixture)


def test_deserialization(mocker):

    mocker.patch.object(json, "loads", return_value=volume_fixture)

    assert Volume.from_json(jsonstr=volume_fixture_json) is not None

    json.loads.assert_called_with(volume_fixture_json)


def test_serialization(mocker):

    mocker.patch.object(json, "dumps", return_value=volume_fixture_json)

    service_entry_point = Volume.from_dict(data=volume_fixture)

    assert service_entry_point.as_json(compact=True) is not None
    json.dumps.assert_called_with(volume_fixture, sort_keys=True)

    assert service_entry_point.as_json() is not None
    json.dumps.assert_called_with(volume_fixture, indent=4, sort_keys=True)
