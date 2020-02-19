#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

from storyhub.sdk.ServiceWrapper import ServiceWrapper
from storyhub.sdk.StoryscriptHub import StoryscriptHub


def update_hub_fixture():
    fixture_dir = path.dirname(path.realpath(__file__))
    out_file = path.join(fixture_dir, "hub.fixed.json")

    services = StoryscriptHub().get_all_service_names()
    ServiceWrapper(services).as_json_file(out_file)


if __name__ == "__main__":
    update_hub_fixture()
