# -*- coding: utf-8 -*-
import tempfile

from asyncy.hub.sdk.AsyncyHub import AsyncyHub
from asyncy.hub.sdk.GraphQL import GraphQL


def test_caching(mocker):
    config = {
        'config_bucket': True
    }
    mocker.patch.object(GraphQL, 'get_all', return_value=[
        {
            'service': {
                'name': 'sample_name',
                'alias': 'sample_alias',
                'owner': {
                    'username': 'default_username'
                },
                'topics': [
                    'the', 'topics', 'are', 'here'
                ],
                'description': 'service_description',
                'isCertified': False,
                'public': True
            },
            'serviceUuid': 'A86742FD-55B4-4AEC-92B9-9989B3AF2F7E',
            'state': 'BETA',
            'configuration': config,
            'readme': 'readme_here'
        },
    ])
    hub = AsyncyHub(db_path=tempfile.mkdtemp())
    hub.update_cache()
    assert hub.get_all_service_names() == ['sample_alias',
                                           'default_username/sample_name']

    service = hub.get(alias='sample_alias')
    assert service.name == 'sample_name'
    assert service.configuration == config

    service = hub.get(owner='default_username', name='sample_name')
    assert service.name == 'sample_name'
    assert service.configuration == config
