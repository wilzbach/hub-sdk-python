import json

from storyscript.hub.sdk.service.Argument import Argument
from storyscript.hub.sdk.service.Action import Action
from storyscript.hub.sdk.service.Event import Event
from storyscript.hub.sdk.service.HttpOptions import HttpOptions
from storyscript.hub.sdk.service.Output import Output

action_fixture = {
    "name": "write",
    "action": {
        "http": {
            "contentType": "application/json",
            "use_action_conn": True
        },
        "arguments": {
            "flush": {
                "in": "responseBody",
                "type": "boolean",
                "required": False
            }
        },
        "events": {
            "listen": {
                "help": "Listen and respond to http connections by\nregistering with the Storyscript Gateway resulting in a serverless function.\n",
                "http": {
                    "port": 8889,
                    "subscribe": {
                        "path": "/register",
                        "method": "post",
                        "contentType": "application/json"
                    },
                    "unsubscribe": {
                        "path": "/unregister",
                        "method": "post",
                        "contentType": "application/json"
                    }
                },
                "output": {
                    "type": "object",
                    "actions": {
                        "flush": {
                            "http": {
                                "contentType": "application/json",
                                "use_event_conn": True
                            }
                        },
                        "write": {
                            "http": {
                                "contentType": "application/json",
                                "use_event_conn": True
                            },
                            "arguments": {
                                "flush": {
                                    "in": "responseBody",
                                    "type": "boolean",
                                    "required": True
                                },
                                "content": {
                                    "in": "responseBody",
                                    "type": "string",
                                    "required": True
                                }
                            }
                        },
                        "finish": {
                            "http": {
                                "contentType": "application/json",
                                "use_event_conn": True
                            }
                        },
                        "redirect": {
                            "help": "Redirect the incoming URL. No additional actions may be used after executing this command.",
                            "http": {
                                "contentType": "application/json",
                                "use_event_conn": True
                            },
                            "arguments": {
                                "url": {
                                    "in": "responseBody",
                                    "type": "string",
                                    "required": True
                                },
                                "query": {
                                    "in": "responseBody",
                                    "help": "These query parameters are appended to the URL specified.",
                                    "type": "map"
                                }
                            }
                        },
                        "get_header": {
                            "http": {
                                "contentType": "application/json",
                                "use_event_conn": True
                            },
                            "arguments": {
                                "key": {
                                    "in": "responseBody",
                                    "type": "string",
                                    "required": True
                                }
                            }
                        },
                        "set_header": {
                            "http": {
                                "contentType": "application/json",
                                "use_event_conn": True
                            },
                            "arguments": {
                                "key": {
                                    "in": "responseBody",
                                    "type": "string",
                                    "required": True
                                },
                                "value": {
                                    "in": "responseBody",
                                    "type": "string",
                                    "required": True
                                }
                            }
                        },
                        "set_status": {
                            "http": {
                                "contentType": "application/json",
                                "use_event_conn": True
                            },
                            "arguments": {
                                "code": {
                                    "in": "responseBody",
                                    "type": "int",
                                    "required": True
                                }
                            }
                        }
                    },
                    "properties": {
                        "uri": {
                            "help": "The URI of the incoming HTTP request",
                            "type": "string"
                        },
                        "body": {
                            "help": "The JSON body of the incoming HTTP request",
                            "type": "map"
                        },
                        "path": {
                            "help": "The path portion of th URI of the incoming HTTP request",
                            "type": "string"
                        },
                        "headers": {
                            "help": "The HTTP headers of the incoming HTTP request",
                            "type": "map"
                        },
                        "query_params": {
                            "help": "The parsed query parameters of the HTTP request",
                            "type": "map"
                        }
                    },
                    "contentType": "application/json"
                },
                "arguments": {
                    "path": {
                        "in": "requestBody",
                        "type": "string",
                        "required": True
                    },
                    "method": {
                        "in": "requestBody",
                        "enum": [
                            "get",
                            "post",
                            "patch",
                            "delete",
                            "put",
                            "options"
                        ],
                        "type": "string",
                        "default": "get"
                    }
                }
            }
        },
        "output": {
            "type": "object",
            "actions": {
                "redirect": {
                    "help": "Redirect the incoming URL. No additional actions may be used after executing this command.",
                    "http": {
                        "contentType": "application/json",
                        "use_event_conn": True
                    },
                    "arguments": {
                        "url": {
                            "in": "responseBody",
                            "type": "string",
                            "required": True
                        },
                        "query": {
                            "in": "responseBody",
                            "help": "These query parameters are appended to the URL specified.",
                            "type": "map"
                        }
                    }
                }
            },
            "properties": {
                "path": {
                    "help": "The path portion of th URI of the incoming HTTP request",
                    "type": "string"
                }
            },
            "contentType": "application/json"
        }

    }
}

action_fixture_json = json.dumps(action_fixture)


def test_deserialization(mocker):

    mocker.patch.object(json, 'loads', return_value=action_fixture)

    mocker.patch.object(Argument, 'from_dict')
    mocker.patch.object(Event, 'from_dict')
    mocker.patch.object(HttpOptions, 'from_dict')
    mocker.patch.object(Output, 'from_dict')


    assert Action.from_json(jsonstr=action_fixture_json) is not None

    json.loads.assert_called_with(action_fixture_json)

    Argument.from_dict.assert_any_call(data={
        "name": "flush",
        "argument": action_fixture["action"]["arguments"]["flush"]
    })

    HttpOptions.from_dict.assert_any_call(data={
        "http_options": action_fixture["action"]["http"]
    })

    Event.from_dict.assert_called_with(data={
        "name": "listen",
        "event": action_fixture["action"]["events"]["listen"]
    })

    Output.from_dict.assert_any_call(data={
        "output": action_fixture["action"]["output"]
    })


def test_serialization(mocker):

    mocker.patch.object(json, 'dumps', return_value=action_fixture_json)

    service_action = Action.from_dict(data=action_fixture)

    assert service_action.as_json(compact=True) is not None
    json.dumps.assert_called_with(action_fixture, sort_keys=True)

    assert service_action.as_json() is not None
    json.dumps.assert_called_with(action_fixture, indent=4, sort_keys=True)

