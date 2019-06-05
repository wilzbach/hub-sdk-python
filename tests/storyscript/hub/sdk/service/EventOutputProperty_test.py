import json

from storyscript.hub.sdk.service.EventOutput import EventOutput

event_output_property_fixture = {
    "name": "query_params",
    "event_property": {
        "help": "The parsed query parameters of the HTTP request",
        "type": "map"
    }
}

event_output_property_fixture_json = json.dumps(event_output_property_fixture)


def test_deserialization(mocker):
    mocker.patch.object(json, 'loads', return_value=event_output_property_fixture)

    assert EventOutput.from_json(jsonstr=event_output_property_fixture_json) is not None

    json.loads.assert_called_with(event_output_property_fixture_json)


def test_serialization(mocker):
    mocker.patch.object(json, 'dumps', return_value=event_output_property_fixture_json)

    service_event = EventOutput.from_dict(data=event_output_property_fixture)

    assert service_event.as_json(compact=True) is not None
    json.dumps.assert_called_with(event_output_property_fixture, sort_keys=True)

    assert service_event.as_json() is not None
    json.dumps.assert_called_with(event_output_property_fixture, indent=4, sort_keys=True)
