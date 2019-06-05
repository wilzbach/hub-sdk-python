import json

from storyscript.hub.sdk.service.Action import Action
from storyscript.hub.sdk.service.Command import Command
from storyscript.hub.sdk.service.Configuration import Configuration
from storyscript.hub.sdk.service.Entrypoint import Entrypoint
from storyscript.hub.sdk.service.EnvironmentVariable import EnvironmentVariable
from storyscript.hub.sdk.service.HubService import HubService
from storyscript.hub.sdk.service.Lifecycle import Lifecycle
from storyscript.hub.sdk.service.ServiceInfo import ServiceInfo
from storyscript.hub.sdk.service.Volume import Volume

configuration_fixture= {
    "configuration": {
        "omg": 1,
        "actions": {
            "help": "Make http calls and listen for http connections through the Storyscript Gateway\nresulting in serverless http endpoints.\n",
            "fetch": {
                "help": "Make a HTTP request to the outside world.\nThis command is native to the platform for performance reasons.\n",
                "output": {
                    "type": "any"
                },
                "arguments": {
                    "url": {
                        "in": "requestBody",
                        "type": "string",
                        "required": True
                    },
                    "body": {
                        "in": "requestBody",
                        "type": "any"
                    },
                    "query": {
                        "in": "requestBody",
                        "help": "Set an optional map of query parameters.\nQuery parameters are automatically appended to the url specified (/url?foo=bar&john=doe)\n",
                        "type": "map"
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
                    },
                    "headers": {
                        "in": "requestBody",
                        "type": "map"
                    }
                }
            },
            "server": {
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
                }
            }
        },
        "entrypoint": {
            "help": "Does nothing",
            "arguments": {
                "path": {
                    "help": "Nothing to see here",
                    "type": "string",
                    "required": True
                }
            }
        },
        "commands": {
            "read": {
                "output": {
                    "type": "any"
                },
                "arguments": {
                    "path": {
                        "type": "string",
                        "required": True
                    }
                }
            }
        },
        "volumes": {
            "py": {
                "target": "/data"
            }
        },
        "info": {
            "title": "Stockbroker",
            "license": {
                "url": "https://opensource.org/licenses/MIT",
                "name": "MIT"
            },
            "version": "0.0.1",
            "description": "An http service to fetch stock prices",
            "contact": {
                "url": "https://storyscript.io",
                "name": "Aurelien ARINO",
                "email": "aurelien@storyscript.io"
            }
        },
        "expose": {
            "v1_api": {
                "http": {
                    "path": "/v1",
                    "port": 8080
                }
            },
            "console": {
                "http": {
                    "path": "/console",
                    "port": 8080
                }
            },
            "graphql": {
                "http": {
                    "path": "/v1alpha1",
                    "port": 8080
                }
            }
        },
        "lifecycle": {
            "startup": {
                "command": [
                    "/bin/graphql-engine",
                    "serve"
                ]
            }
        },
        "environment": {
            "HASURA_GRAPHQL_DATABASE_URL": {
                "help": "The URL to your postgres database, such as postgres://user:password@host/database_name",
                "type": "string",
                "required": True
            },
            "HASURA_GRAPHQL_ENABLE_CONSOLE": {
                "help": "Whether to enable the built in console or not",
                "type": "boolean",
                "default": True,
                "required": True
            }
        }
    }
}

configuration_fixture_json = json.dumps(configuration_fixture)


def test_deserialization(mocker):
    mocker.patch.object(json, 'loads', return_value=configuration_fixture)

    mocker.patch.object(Entrypoint, 'from_dict')
    mocker.patch.object(Action, 'from_dict')
    mocker.patch.object(Command, 'from_dict')
    mocker.patch.object(Volume, 'from_dict')
    mocker.patch.object(EnvironmentVariable, 'from_dict')
    mocker.patch.object(Lifecycle, 'from_dict')
    mocker.patch.object(ServiceInfo, 'from_dict')

    configuration = Configuration.from_json(configuration_fixture_json)

    assert configuration is not None

    json.loads.assert_called_with(configuration_fixture_json)

    Entrypoint.from_dict.assert_called_once_with(data={
        "entrypoint": configuration_fixture["configuration"]["entrypoint"]
    })

    Action.from_dict.assert_any_call(data={
        "name": "fetch",
        "action": configuration_fixture["configuration"]["actions"]["fetch"]
    })

    Command.from_dict.assert_any_call(data={
        "name": "read",
        "command": configuration_fixture["configuration"]["commands"]["read"]
    })

    Volume.from_dict.assert_any_call(data={
        "name": "py",
        "volume": configuration_fixture["configuration"]["volumes"]["py"]
    })

    EnvironmentVariable.from_dict.assert_any_call(data={
        "name": "HASURA_GRAPHQL_ENABLE_CONSOLE",
        "environment_variable": configuration_fixture["configuration"]["environment"]["HASURA_GRAPHQL_ENABLE_CONSOLE"]
    })

    Lifecycle.from_dict.assert_called_once_with(data={
        "lifecycle": configuration_fixture["configuration"]["lifecycle"]
    })

    ServiceInfo.from_dict.assert_called_once_with(data={
        "service_info": configuration_fixture["configuration"]["info"]
    })


def test_serialization(mocker):
    mocker.patch.object(json, 'dumps', return_value=configuration_fixture_json)

    configuration = Configuration.from_dict(data=configuration_fixture)

    # ensure that the compact option works
    assert configuration.as_json(compact=True) is not None
    json.dumps.assert_called_with(configuration_fixture, sort_keys=True)

    assert configuration.as_json() is not None
    json.dumps.assert_called_with(configuration_fixture, indent=4, sort_keys=True)
