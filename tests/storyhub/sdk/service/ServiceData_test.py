import json

from storyhub.sdk.service.Configuration import Configuration
from storyhub.sdk.service.Service import Service
from storyhub.sdk.service.ServiceData import ServiceData
from tests.storyhub.sdk.JsonFixtureHelper import JsonFixtureHelper

service_data_fixture = JsonFixtureHelper.load_fixture("service_data_fixture")

service_data_fixture_json = json.dumps(service_data_fixture)


def test_deserialization(mocker):
    mocker.patch.object(json, 'loads', return_value=service_data_fixture)

    mocker.patch.object(Configuration, 'from_dict')
    mocker.patch.object(Service, 'from_dict')

    service_data = ServiceData.from_json(service_data_fixture_json)

    assert service_data is not None

    json.loads.assert_called_with(service_data_fixture_json)

    Configuration.from_dict.assert_called_once_with(data={
        "configuration": service_data_fixture["service_data"]["configuration"]
    })

    Service.from_dict.assert_called_once_with(data={
        "service": service_data_fixture["service_data"]["service"]
    })


def test_serialization(mocker):
    mocker.patch.object(json, 'dumps', return_value=service_data_fixture_json)

    service_data = ServiceData.from_dict(data=service_data_fixture)

    # ensure that the compact option works
    assert service_data.as_json(compact=True) is not None
    json.dumps.assert_called_with(service_data_fixture, sort_keys=True)

    assert service_data.as_json() is not None
    json.dumps.assert_called_with(service_data_fixture, indent=4, sort_keys=True)
