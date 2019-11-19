import json

from storyhub.sdk.service.LifecycleOption import LifecycleOption
from tests.storyhub.sdk.JsonFixtureHelper import JsonFixtureHelper

lifecycle_option_fixture = JsonFixtureHelper.load_fixture(
    "lifecycle_option_fixture"
)

lifecycle_option_fixture_json = json.dumps(lifecycle_option_fixture)


def test_deserialization(mocker):

    mocker.patch.object(json, "loads", return_value=lifecycle_option_fixture)

    assert (
        LifecycleOption.from_json(jsonstr=lifecycle_option_fixture_json)
        is not None
    )

    json.loads.assert_called_with(lifecycle_option_fixture_json)


def test_serialization(mocker):

    mocker.patch.object(
        json, "dumps", return_value=lifecycle_option_fixture_json
    )

    service_command = LifecycleOption.from_dict(data=lifecycle_option_fixture)

    assert service_command.as_json(compact=True) is not None
    json.dumps.assert_called_with(lifecycle_option_fixture, sort_keys=True)

    assert service_command.as_json() is not None
    json.dumps.assert_called_with(
        lifecycle_option_fixture, indent=4, sort_keys=True
    )
