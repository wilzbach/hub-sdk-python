import json

from storyhub.sdk.service.Action import Action
from storyhub.sdk.service.Argument import Argument
from storyhub.sdk.service.Event import Event
from storyhub.sdk.service.HttpOptions import HttpOptions
from storyhub.sdk.service.ServiceOutput import ServiceOutput
from tests.storyhub.sdk.JsonFixtureHelper import JsonFixtureHelper

event_fixture = JsonFixtureHelper.load_fixture("event_fixture")

event_fixture_json = json.dumps(event_fixture)


def test_deserialization(mocker):
    mocker.patch.object(json, 'loads', return_value=event_fixture)

    mocker.patch.object(Argument, 'from_dict')
    mocker.patch.object(Action, 'from_dict')
    mocker.patch.object(ServiceOutput, 'from_dict')
    mocker.patch.object(HttpOptions, 'from_dict')

    assert Event.from_json(jsonstr=event_fixture_json) is not None

    json.loads.assert_called_with(event_fixture_json)

    Argument.from_dict.assert_any_call(data={
        "name": "path",
        "argument": event_fixture["event"]["arguments"]["path"]
    })

    ServiceOutput.from_dict.assert_any_call(data={
        "output": event_fixture["event"]["output"]
    })

    HttpOptions.from_dict.assert_called_once_with(data={
        "http_options": event_fixture["event"]["http"]
    })


def test_serialization(mocker):
    mocker.patch.object(json, 'dumps', return_value=event_fixture_json)

    service_event = Event.from_dict(data=event_fixture)

    assert service_event.as_json(compact=True) is not None
    json.dumps.assert_called_with(event_fixture, sort_keys=True)

    assert service_event.as_json() is not None
    json.dumps.assert_called_with(event_fixture, indent=4, sort_keys=True)


def test_getters(mocker):
    service_event = Event.from_json(jsonstr=event_fixture_json)

    assert service_event.help() == event_fixture['event']['help']
