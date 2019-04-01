# -*- coding: utf-8 -*-
from asyncy.hub.sdk.GraphQL import GraphQL


def test_get_all():
    services = GraphQL.get_all()
    assert len(services) > 10  # Because the Hub has at least 10.
