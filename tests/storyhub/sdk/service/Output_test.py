import json

from storyhub.sdk.service.Output import Output
from storyhub.sdk.service.OutputAction import OutputAction
from storyhub.sdk.service.OutputProperty import OutputProperty
from tests.storyhub.sdk.JsonFixtureHelper import JsonFixtureHelper

output_fixture = JsonFixtureHelper.load_fixture("output_fixture")

output_fixture_json = json.dumps(output_fixture)


def test_deserialization(mocker):
    mocker.patch.object(json, 'loads', return_value=output_fixture)

    mocker.patch.object(OutputAction, 'from_dict')
    mocker.patch.object(OutputProperty, 'from_dict')

    output = Output.from_json(jsonstr=output_fixture_json)

    assert output is not None

    json.loads.assert_called_with(output_fixture_json)

    assert output.type() == output_fixture["output"]["type"]
    assert output.content_type() == output_fixture["output"]["contentType"]

    OutputAction.from_dict.assert_any_call(data={
        "name": "write",
        "output_action": output_fixture["output"]["actions"]["write"]
    })

    OutputProperty.from_dict.assert_called_once_with(data={
        "name": "query_params",
        "output_property": output_fixture["output"]["properties"]["query_params"]
    })


def test_serialization(mocker):
    mocker.patch.object(json, 'dumps', return_value=output_fixture_json)

    service_event = Output.from_dict(data=output_fixture)

    assert service_event.as_json(compact=True) is not None
    json.dumps.assert_called_with(output_fixture, sort_keys=True)

    assert service_event.as_json() is not None
    json.dumps.assert_called_with(output_fixture, indent=4, sort_keys=True)
