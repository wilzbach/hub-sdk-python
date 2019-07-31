import json

from storyhub.sdk.service.Action import Action
from storyhub.sdk.service.Argument import Argument
from storyhub.sdk.service.Event import Event
from storyhub.sdk.service.HttpOptions import HttpOptions
from storyhub.sdk.service.Output import Output
from tests.storyhub.sdk.JsonFixtureHelper import JsonFixtureHelper

action_fixture = JsonFixtureHelper.load_fixture("action_fixture")

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

