# -*- coding: utf-8 -*-
import tempfile

from asyncy.hub.sdk.AsyncyHub import AsyncyHub
from asyncy.hub.sdk.GraphQL import GraphQL


def test_caching(mocker):
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
            'serviceUuid': 'service_uuid',
            'state': 'BETA',
            'configuration': {
                'config_bucket': True
            },
            'readme': 'readme_here'
        },
    ])
    hub = AsyncyHub(db_path=tempfile.mkdtemp())
    hub.update_cache()
    assert hub.get_all_service_names() == ['sample_alias',
                                           'default_username/sample_name']
