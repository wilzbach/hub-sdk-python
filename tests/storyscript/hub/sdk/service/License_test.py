import json

from storyscript.hub.sdk.service.License import License

license_fixture = {
    "license": {
        "url": "https://opensource.org/licenses/MIT",
        "name": "MIT"
    }
}

license_fixture_json = json.dumps(license_fixture)


def test_deserialization(mocker):

    mocker.patch.object(json, 'loads', return_value=license_fixture)

    assert License.from_json(jsonstr=license_fixture_json) is not None

    json.loads.assert_called_with(license_fixture_json)


def test_serialization(mocker):

    mocker.patch.object(json, 'dumps', return_value=license_fixture_json)

    service_command = License.from_dict(data=license_fixture)

    assert service_command.as_json(compact=True) is not None
    json.dumps.assert_called_with(license_fixture, sort_keys=True)

    assert service_command.as_json() is not None
    json.dumps.assert_called_with(license_fixture, indent=4, sort_keys=True)