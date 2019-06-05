import json

from storyscript.hub.sdk.service.EventOutput import EventOutput
from storyscript.hub.sdk.service.EventOutputAction import EventOutputAction
from storyscript.hub.sdk.service.EventOutputProperty import EventOutputProperty

event_output_fixture = {
    "event_output": {
        "type": "object",
        "actions": {
            "write": {
                "http": {
                    "path": "/digest",
                    "port": 8080,
                    "method": "post",
                    "contentType": "application/json",
                    "use_event_conn": True,
                    "subscribe": {
                        "path": "/stream/subscribe",
                        "method": "post",
                        "contentType": "application/json"
                    },
                    "unsubscribe": {
                        "path": "/stream/unsubscribe",
                        "method": "post"
                    }
                },
                "arguments": {
                    "flush": {
                        "in": "responseBody",
                        "type": "boolean",
                        "required": False
                    }
                }
            }
        },
        "properties": {
            "query_params": {
                "help": "The parsed query parameters of the HTTP request",
                "type": "map"
            }
        },
        "contentType": "application/json"
    },
}

event_output_fixture_json = json.dumps(event_output_fixture)


def test_deserialization(mocker):
    mocker.patch.object(json, 'loads', return_value=event_output_fixture)

    mocker.patch.object(EventOutputAction, 'from_dict')
    mocker.patch.object(EventOutputProperty, 'from_dict')

    assert EventOutput.from_json(jsonstr=event_output_fixture_json) is not None

    json.loads.assert_called_with(event_output_fixture_json)

    EventOutputAction.from_dict.assert_any_call(data={
        "name": "write",
        "output_action": event_output_fixture["event_output"]["actions"]["write"]
    })

    EventOutputProperty.from_dict.assert_called_once_with(data={
        "name": "query_params",
        "output_property": event_output_fixture["event_output"]["properties"]["query_params"]
    })


def test_serialization(mocker):
    mocker.patch.object(json, 'dumps', return_value=event_output_fixture_json)

    service_event = EventOutput.from_dict(data=event_output_fixture)

    assert service_event.as_json(compact=True) is not None
    json.dumps.assert_called_with(event_output_fixture, sort_keys=True)

    assert service_event.as_json() is not None
    json.dumps.assert_called_with(event_output_fixture, indent=4, sort_keys=True)
