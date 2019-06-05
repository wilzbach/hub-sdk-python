import json

from storyscript.hub.sdk.service.Action import Action
from storyscript.hub.sdk.service.Command import Command
from storyscript.hub.sdk.service.Configuration import Configuration
from storyscript.hub.sdk.service.Entrypoint import Entrypoint
from storyscript.hub.sdk.service.HubService import HubService
from storyscript.hub.sdk.service.Volume import Volume

hub_service_fixture = {
    "hub_service": {
        "service": {
            "name": "file",
            "alias": "file",
            "owner": {
                "username": "storyscript"
            },
            "topics": [],
            "description": "The microservice yaml for `file` -- An internal Storyscript service",
            "isCertified": True,
            "public": True
        },
        "serviceUuid": "1b3a1a21-4083-4138-b708-7909663f5549",
        "state": "BETA",
        "configuration": {
            "volumes": {
                "py": {
                    "target": "/data"
                }
            },
            "actions": {
                "fetch": {
                    "help": "Does nothing",
                    "format": {
                        "command": [
                            "/nothing"
                        ]
                    },
                    "output": {
                        "type": "float"
                    },
                    "arguments": {
                        "something": {
                            "help": "just a string",
                            "type": "string",
                            "required": True
                        }
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
            "entrypoint": {
                "help": "Does nothing",
                "arguments": {
                    "path": {
                        "help": "Nothing to see here",
                        "type": "string",
                        "required": True
                    }
                }
            }
        },
        "readme": "Nothing to see here"
    }
}

hub_service_fixture= {
    "hub_service": {
        "service": {
            "name": "http",
            "alias": "http",
            "owner": {
                "username": "storyscript"
            },
            "topics": [
                "omg",
                "storyscript",
                "microservice"
            ],
            "description": "The Storyscript API gateway server for executing Stories via HTTP.",
            "isCertified": True,
            "public": True
        },
        "serviceUuid": "18564840-7551-4bb7-9ba7-bb9c9e2d92b4",
        "state": "BETA",
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
                "description": "An http service to fetch stock prices"
            }
        },
        "readme": "# Storyscript HTTP Gateway\n\nAPI gateway server for executing Stories via HTTP.\n\n```coffee\nhttp server as server\n  when server listen method:'get' path:'/' as r\n    log info msg:r.body\n    log info msg:r.headers\n    log info msg:r.headers['Host']\n    r write data:'Hello World'\n    r status code:200\n    r finish\n```\n\n```sh\n$ curl https://foobar.storyscriptapp.com/\nHello World\n```\n\n\n## Development\n\nSetup virtual environment and install dependencies\n```\nvirtualenv -p python3.6 venv\nsource venv/bin/activate\npip install -r requirements.txt\n```\n\nRun locally by calling\n\n```\npython -m app.main --logging=debug --debug\n```\n\n### Register an endpoint\n\n```shell\ncurl --data '{\"endpoint\": \"http://localhost:9000/story/foo\", \"data\":{\"path\":\"/ping\", \"method\": \"post\", \"host\": \"a\"}}' \\\n     -H \"Content-Type: application/json\" \\\n     localhost:8889/register\n```\n\nNow access that endpoint\n\n```shell\ncurl -X POST -d 'foobar' -H \"Host: a.storyscriptapp.com\" http://localhost:8888/ping\n```\n\n\n### Unregister an endpoint\n\n```shell\ncurl --data '{\"endpoint\": \"http://localhost:9000/story/foo\", \"data\":{\"path\":\"/ping\", \"method\": \"post\", \"host\": \"a\"}}' \\\n     -H \"Content-Type: application/json\" \\\n     localhost:8889/unregister\n```\n"
    }
}

hub_service_fixture_json = json.dumps(hub_service_fixture)


def test_deserialization(mocker):
    mocker.patch.object(json, 'loads', return_value=hub_service_fixture)

    mocker.patch.object(Configuration, 'from_dict')

    hub_service = HubService.from_json(hub_service_fixture_json)

    assert hub_service is not None

    json.loads.assert_called_with(hub_service_fixture_json)

    Configuration.from_dict.assert_called_once_with(data={
        "configuration": hub_service_fixture["hub_service"]["configuration"]
    })


def test_serialization(mocker):
    mocker.patch.object(json, 'dumps', return_value=hub_service_fixture_json)

    hub_service = HubService.from_dict(data=hub_service_fixture)

    # ensure that the compact option works
    assert hub_service.as_json(compact=True) is not None
    json.dumps.assert_called_with(hub_service_fixture, sort_keys=True)

    assert hub_service.as_json() is not None
    json.dumps.assert_called_with(hub_service_fixture, indent=4, sort_keys=True)
