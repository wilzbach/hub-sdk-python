import json

from storyhub.sdk.service.Lifecycle import Lifecycle
from storyhub.sdk.service.LifecycleOption import (
    LifecycleOption,
    LifecycleOptionType,
)
from tests.storyhub.sdk.JsonFixtureHelper import JsonFixtureHelper

lifecycle_fixture = JsonFixtureHelper.load_fixture("lifecycle_fixture")

lifecycle_fixture_json = json.dumps(lifecycle_fixture)


def test_deserialization(mocker):
    mocker.patch.object(json, "loads", return_value=lifecycle_fixture)

    mocker.patch.object(LifecycleOption, "from_dict")

    assert Lifecycle.from_json(jsonstr=lifecycle_fixture_json) is not None

    json.loads.assert_called_with(lifecycle_fixture_json)

    LifecycleOption.from_dict.assert_called_with(
        data={
            "type": LifecycleOptionType.STARTUP,
            "lifecycle_option": lifecycle_fixture["lifecycle"]["startup"],
        }
    )


def test_serialization(mocker):
    mocker.patch.object(json, "dumps", return_value=lifecycle_fixture_json)

    service_command = Lifecycle.from_dict(data=lifecycle_fixture)

    assert service_command.as_json(compact=True) is not None
    json.dumps.assert_called_with(lifecycle_fixture, sort_keys=True)

    assert service_command.as_json() is not None
    json.dumps.assert_called_with(lifecycle_fixture, indent=4, sort_keys=True)
