import json

from storyhub.sdk.service.HttpOptions import HttpOptions
from tests.storyhub.sdk.JsonFixtureHelper import JsonFixtureHelper

http_options_fixture = JsonFixtureHelper.load_fixture("http_option_fixture")
http_options_fixture_json = json.dumps(http_options_fixture)


def test_deserialization(mocker):
    mocker.patch.object(json, "loads", return_value=http_options_fixture)

    http_options = HttpOptions.from_json(jsonstr=http_options_fixture_json)

    assert http_options is not None

    json.loads.assert_called_with(http_options_fixture_json)

    subscribe = HttpOptions.from_dict(
        data={
            "http_options": http_options_fixture["http_options"]["subscribe"]
        }
    )

    unsubscribe = HttpOptions.from_dict(
        data={
            "http_options": http_options_fixture["http_options"]["unsubscribe"]
        }
    )

    assert http_options.subscribe().path() == subscribe.path()
    assert http_options.subscribe().method() == subscribe.method()
    assert http_options.subscribe().content_type() == subscribe.content_type()

    assert http_options.unsubscribe().path() == unsubscribe.path()
    assert http_options.unsubscribe().method() == unsubscribe.method()
    assert (
        http_options.unsubscribe().content_type() == unsubscribe.content_type()
    )


def test_serialization(mocker):
    mocker.patch.object(json, "dumps", return_value=http_options_fixture_json)

    service_event = HttpOptions.from_dict(data=http_options_fixture)

    assert service_event.as_json(compact=True) is not None
    json.dumps.assert_called_with(http_options_fixture, sort_keys=True)

    assert service_event.as_json() is not None
    json.dumps.assert_called_with(
        http_options_fixture, indent=4, sort_keys=True
    )
