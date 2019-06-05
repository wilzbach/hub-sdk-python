import json

# todo needs improvements
from storyscript.hub.sdk.service.Argument import Argument
from storyscript.hub.sdk.service.EventOutput import EventOutput
from storyscript.hub.sdk.service.HttpOptions import HttpOptions

event_output_action_fixture = {
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

event_output_action_fixture_json = json.dumps(event_output_action_fixture)


def test_deserialization(mocker):
    mocker.patch.object(json, 'loads', return_value=event_output_action_fixture)

    mocker.patch.object(HttpOptions, 'from_dict')
    mocker.patch.object(Argument, 'from_dict')

    assert EventOutput.from_json(jsonstr=event_output_action_fixture_json) is not None

    json.loads.assert_called_with(event_output_action_fixture_json)

    HttpOptions.from_dict.assert_called_with(data={
        "http_options": event_output_action_fixture["event_output"]["actions"]["write"]["http"]
    })


def test_serialization(mocker):
    mocker.patch.object(json, 'dumps', return_value=event_output_action_fixture_json)

    service_event = EventOutput.from_dict(data=event_output_action_fixture)

    assert service_event.as_json(compact=True) is not None
    json.dumps.assert_called_with(event_output_action_fixture, sort_keys=True)

    assert service_event.as_json() is not None
    json.dumps.assert_called_with(event_output_action_fixture, indent=4, sort_keys=True)
