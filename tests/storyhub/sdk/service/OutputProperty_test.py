import json

from storyhub.sdk.service.OutputProperty import OutputProperty
from tests.storyhub.sdk.JsonFixtureHelper import JsonFixtureHelper

output_property_fixture = JsonFixtureHelper.load_fixture("output_property_fixture")

output_property_fixture_json = json.dumps(output_property_fixture)


def test_deserialization(mocker):
    mocker.patch.object(json, 'loads', return_value=output_property_fixture)

    assert OutputProperty.from_json(jsonstr=output_property_fixture_json) is not None

    json.loads.assert_called_with(output_property_fixture_json)


def test_serialization(mocker):
    mocker.patch.object(json, 'dumps', return_value=output_property_fixture_json)

    service_event = OutputProperty.from_dict(data=output_property_fixture)

    assert service_event.as_json(compact=True) is not None
    json.dumps.assert_called_with(output_property_fixture, sort_keys=True)

    assert service_event.as_json() is not None
    json.dumps.assert_called_with(output_property_fixture, indent=4, sort_keys=True)


def test_getters(mocker):

    property = OutputProperty.from_json(jsonstr=output_property_fixture_json)

    assert property.type() == \
        output_property_fixture['output_property']['type']

    assert property.name() == output_property_fixture["name"]
