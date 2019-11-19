import json

from storyhub.sdk.service.output import (
    OutputAny,
    OutputBoolean,
    OutputEnum,
    OutputFloat,
    OutputInt,
    OutputList,
    OutputMap,
    OutputRegex,
    OutputNone,
    OutputObject,
    OutputString,
)
from storyhub.sdk.service.output.OutputUtils import OutputUtils
from tests.storyhub.sdk.JsonFixtureHelper import JsonFixtureHelper

output_object_fixture = JsonFixtureHelper.load_fixture("output_object_fixture")

output_object_fixture_json = json.dumps(output_object_fixture)


def test_deserialization(mocker):
    mocker.patch.object(json, 'loads', return_value=output_object_fixture)

    assert OutputObject.from_json(jsonstr=output_object_fixture_json) \
        is not None

    json.loads.assert_called_with(output_object_fixture_json)


def test_serialization(mocker):
    mocker.patch.object(json, 'dumps', return_value=output_object_fixture_json)

    service_event = OutputUtils.parse_type(output_object_fixture)

    assert service_event.as_json(compact=True) is not None
    json.dumps.assert_called_with(output_object_fixture, sort_keys=True)

    assert service_event.as_json() is not None
    json.dumps.assert_called_with(output_object_fixture, indent=4,
                                  sort_keys=True)


def test_getters(mocker):

    property = OutputObject.from_json(jsonstr=output_object_fixture_json)

    assert isinstance(property, OutputObject)

    assert property.name() == output_object_fixture['name']

    assert property.help() == 'No help available'

    out_props = output_object_fixture['properties']

    props = property.properties()
    assert len(props) == 15

    assert isinstance(props['uri'], OutputString)
    props['uri'].help() == out_props['uri']['help']

    assert isinstance(props['body'], OutputMap)
    props['body'].help() == out_props['body']['help']
    assert isinstance(props['body'].keys(), OutputAny)
    assert isinstance(props['body'].values(), OutputAny)

    assert isinstance(props['path'], OutputString)
    props['path'].help() == out_props['path']['help']

    assert isinstance(props['query_params'], OutputMap)
    props['query_params'].help() == \
        out_props['query_params']['help']
    assert isinstance(props['query_params'].keys(), OutputString)
    assert isinstance(props['query_params'].values(), OutputString)

    assert isinstance(props['re'], OutputRegex)
    props['re'].help() == out_props['re']['help']

    assert isinstance(props['_int'], OutputInt)
    props['_int'].help() == out_props['_int']['help']

    assert isinstance(props['_float'], OutputFloat)
    props['_float'].help() == out_props['_float']['help']

    assert isinstance(props['_number'], OutputInt)
    props['_number'].help() == out_props['_number']['help']

    assert isinstance(props['_any'], OutputAny)
    props['_any'].help() == out_props['_any']['help']

    assert isinstance(props['_list_any'], OutputList)
    props['_list_any'].help() == out_props['_list_any']['help']
    assert isinstance(props['_list_any'].elements(), OutputAny)

    assert isinstance(props['_list_str'], OutputList)
    props['_list_str'].help() == out_props['_list_str']['help']
    assert isinstance(props['_list_str'].elements(), OutputString)

    assert isinstance(props['_boolean'], OutputBoolean)
    props['_boolean'].help() == out_props['_boolean']['help']

    assert isinstance(props['_none'], OutputNone)
    props['_none'].help() == out_props['_none']['help']

    assert isinstance(props['_enum'], OutputEnum)
    props['_enum'].help() == out_props['_enum']['help']
    props['_enum'].enum() == out_props['_enum']['enum']

    assert isinstance(props['_object_no_props'], OutputObject)
    assert props['_object_no_props'].properties() == {}
