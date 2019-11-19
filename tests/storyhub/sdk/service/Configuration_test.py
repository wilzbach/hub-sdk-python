import json

from storyhub.sdk.service.Action import Action
from storyhub.sdk.service.Command import Command
from storyhub.sdk.service.Configuration import Configuration
from storyhub.sdk.service.Entrypoint import Entrypoint
from storyhub.sdk.service.EnvironmentVariable import EnvironmentVariable
from storyhub.sdk.service.Lifecycle import Lifecycle
from storyhub.sdk.service.ServiceInfo import ServiceInfo
from storyhub.sdk.service.Volume import Volume
from tests.storyhub.sdk.JsonFixtureHelper import JsonFixtureHelper

configuration_fixture = JsonFixtureHelper.load_fixture("configuration_fixture")

configuration_fixture_json = json.dumps(configuration_fixture)


def test_deserialization(mocker):
    mocker.patch.object(json, "loads", return_value=configuration_fixture)

    mocker.patch.object(Entrypoint, "from_dict")
    mocker.patch.object(Action, "from_dict")
    mocker.patch.object(Command, "from_dict")
    mocker.patch.object(Volume, "from_dict")
    mocker.patch.object(EnvironmentVariable, "from_dict")
    mocker.patch.object(Lifecycle, "from_dict")
    mocker.patch.object(ServiceInfo, "from_dict")

    configuration = Configuration.from_json(configuration_fixture_json)

    assert configuration is not None

    json.loads.assert_called_with(configuration_fixture_json)

    Entrypoint.from_dict.assert_called_once_with(
        data={
            "entrypoint": configuration_fixture["configuration"]["entrypoint"]
        }
    )

    Action.from_dict.assert_any_call(
        data={
            "name": "fetch",
            "action": configuration_fixture["configuration"]["actions"][
                "fetch"
            ],
        }
    )

    Command.from_dict.assert_any_call(
        data={
            "name": "read",
            "command": configuration_fixture["configuration"]["commands"][
                "read"
            ],
        }
    )

    Volume.from_dict.assert_any_call(
        data={
            "name": "py",
            "volume": configuration_fixture["configuration"]["volumes"]["py"],
        }
    )

    EnvironmentVariable.from_dict.assert_any_call(
        data={
            "name": "HASURA_GRAPHQL_ENABLE_CONSOLE",
            "environment_variable": configuration_fixture["configuration"][
                "environment"
            ]["HASURA_GRAPHQL_ENABLE_CONSOLE"],
        }
    )

    Lifecycle.from_dict.assert_called_once_with(
        data={"lifecycle": configuration_fixture["configuration"]["lifecycle"]}
    )

    ServiceInfo.from_dict.assert_called_once_with(
        data={"service_info": configuration_fixture["configuration"]["info"]}
    )


def test_serialization(mocker):
    mocker.patch.object(json, "dumps", return_value=configuration_fixture_json)

    configuration = Configuration.from_dict(data=configuration_fixture)

    # ensure that the compact option works
    assert configuration.as_json(compact=True) is not None
    json.dumps.assert_called_with(configuration_fixture, sort_keys=True)

    assert configuration.as_json() is not None
    json.dumps.assert_called_with(
        configuration_fixture, indent=4, sort_keys=True
    )
