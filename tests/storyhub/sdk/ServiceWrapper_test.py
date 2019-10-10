import tempfile
import os
import json
from storyhub.sdk.ServiceWrapper import ServiceWrapper
from storyhub.sdk.GraphQL import GraphQL
from storyhub.sdk.service.ServiceData import ServiceData

# note: needs updates/cleanup
from tests.storyhub.sdk.JsonFixtureHelper import JsonFixtureHelper

service_data_fixture = \
    JsonFixtureHelper.load_fixture("wrapper_service_data_fixture")
not_python_fixture = JsonFixtureHelper.load_fixture("not_python_fixture")


def test_deserialization_dict():
    service_datas = JsonFixtureHelper.load_fixture("hello_services")

    hub = ServiceWrapper.from_dict(service_datas)

    assert hub.get_all_service_names() == ["test/helloworld", "hello"]


def test_deserialization_from_file(mocker):
    expected_service_datas = [
        'microservice/python',
        'python',
        'microservice/hashes',
        'storyscript/http',
        'http',
        'test/helloworld',
        'hello']

    temp_file = tempfile.mktemp(suffix=".json")

    with open(temp_file, 'w') as outfile:
        json.dump(service_data_fixture, outfile)

    hub = ServiceWrapper.from_json_file(path=temp_file)

    mocker.patch.object(ServiceData, 'from_dict')

    assert hub.get_all_service_names() == expected_service_datas

    assert hub.get('python') is not None

    ServiceData.from_dict.assert_called_with(
        data={"service_data": service_data_fixture[0]})

    os.remove(path=temp_file)


def test_deserialization_from_json(mocker):
    expected_service_datas = ["microservice/python", "python"]

    jsonstr = json.dumps([service_data_fixture[0]])

    hub = ServiceWrapper.from_json(jsonstr)

    assert hub.get_all_service_names() == expected_service_datas

    mocker.patch.object(ServiceData, 'from_dict')
    assert hub.get('python') is not None

    ServiceData.from_dict.assert_called_with(data={
        "service_data": service_data_fixture[0]
    })


def test_dynamic_loading_with_list_service_names(mocker):
    expected_service_datas = [
        'test/helloworld', 'hello', 'microservice/hashes']

    mocker.patch.object(GraphQL, 'get_all', return_value=service_data_fixture)

    hub = ServiceWrapper(["hello", "microservice/hashes"])

    assert hub.get_all_service_names() == expected_service_datas


def test_reload_services_with_list_dict(mocker):
    expected_service_datas = ['microservice/not_python', 'npython']

    mocker.patch.object(GraphQL, 'get_all', return_value=service_data_fixture)

    hub = ServiceWrapper([not_python_fixture])

    assert hub.get_all_service_names() == expected_service_datas


def test_serialization(mocker):
    expected_service_datas = [
        'test/helloworld',
        'hello',
        'microservice/hashes',
        'microservice/not_python',
        'npython']

    mocker.patch.object(GraphQL, 'get_all', return_value=service_data_fixture)

    hub = ServiceWrapper([
        "hello",
        "microservice/hashes"
    ])

    hub.update_service(not_python_fixture)

    temp_file = tempfile.mktemp(suffix=".json")

    hub.as_json_file(temp_file)

    assert hub.get_all_service_names() == expected_service_datas

    test_hub = ServiceWrapper.from_json_file(path=temp_file)

    assert test_hub.get_all_service_names() == expected_service_datas

    os.remove(temp_file)
