import json

from storyhub.sdk.service.ServiceOutput import ServiceOutput
from storyhub.sdk.service.output.OutputAction import OutputAction
from storyhub.sdk.service.output.OutputUtils import OutputUtils
from tests.storyhub.sdk.JsonFixtureHelper import JsonFixtureHelper

output_fixture = JsonFixtureHelper.load_fixture("output_fixture")

output_fixture_json = json.dumps(output_fixture)


def test_deserialization(mocker):
    mocker.patch.object(json, "loads", return_value=output_fixture)

    mocker.patch.object(OutputAction, "from_dict")
    mocker.patch.object(OutputUtils, "parse_type")

    output = ServiceOutput.from_json(jsonstr=output_fixture_json)

    assert output is not None

    json.loads.assert_called_with(output_fixture_json)

    assert output.content_type() == output_fixture["output"]["contentType"]

    OutputAction.from_dict.assert_any_call(
        data={
            "name": "write",
            "output_action": output_fixture["output"]["actions"]["write"],
        }
    )

    OutputUtils.parse_type.assert_called_once_with(output_fixture["output"])

    assert output.type() == OutputUtils.parse_type()


def test_serialization(mocker):
    mocker.patch.object(json, "dumps", return_value=output_fixture_json)

    service_event = ServiceOutput.from_dict(data=output_fixture)

    assert service_event.as_json(compact=True) is not None
    json.dumps.assert_called_with(output_fixture, sort_keys=True)

    assert service_event.as_json() is not None
    json.dumps.assert_called_with(output_fixture, indent=4, sort_keys=True)
