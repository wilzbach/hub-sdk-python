# -*- coding: utf-8 -*-
import tempfile

# from time import sleep

from storyhub.sdk.StoryscriptHub import (
    ArchivedStoryscriptHub as StoryscriptHub,
)
from storyhub.sdk.GraphQL import GraphQL
from storyhub.sdk.db.Service import Service
from storyhub.sdk.service.ServiceData import ServiceData
from tests.storyhub.sdk.JsonFixtureHelper import JsonFixtureHelper


class VerifiableService:
    def __init__(
        self,
        owner_name: str,
        name: str,
        alias: str,
        topics: [str],
        desc: str,
        certified: bool,
        public: bool,
        uuid: str,
        state: str,
        config: dict,
        readme: str,
    ):
        self.owner_name = owner_name
        self.name = name
        self.alias = alias
        self.topics = topics
        self.desc = desc
        self.certified = certified
        self.public = public
        self.uuid = uuid
        self.state = state
        self.config = config
        self.readme = readme

        self.service = {
            "service": {
                "name": name,
                "alias": alias,
                "owner": {"username": owner_name},
                "topics": topics,
                "description": desc,
                "isCertified": certified,
                "public": public,
            },
            "serviceUuid": uuid,
            "state": state,
            "configuration": config,
            "readme": readme,
        }

    def verify(self, service: ServiceData):
        assert service.name() == self.name
        assert service.service().alias() == self.alias
        assert service.service().owner().username() == self.owner_name
        assert service.service().topics() == self.topics
        assert service.service().description() == self.desc
        assert service.service().certified() == self.certified
        assert service.service().public() == self.public
        assert service.uuid() == self.uuid
        assert service.state() == self.state
        assert (
            service.configuration().actions()[0].name()
            == list(self.config["actions"].keys())[0]
        )
        assert service.readme() == self.readme


"""
Caching and auto-updating is disabled during the migration to the new runtime
def test_caching(mocker):
    config = {"actions": {"foo": "bar"}}

    owner = "default_username"

    actual_service = VerifiableService(
        owner_name=owner,
        name="sample_name",
        alias="sample_alias",
        topics=["the", "topics", "are", "here"],
        desc="service_description",
        certified=False,
        public=True,
        uuid="A86742FD-55B4-4AEC-92B9-9989B3AF2F7E",
        state="BETA",
        config=config,
        readme="readme_here",
    )

    registered_services = [actual_service.service]

    mocker.patch.object(GraphQL, "get_all", return_value=registered_services)
    hub = StoryscriptHub(db_path=tempfile.mkdtemp())
    # No need to call update_cache explicitly, since the background thread will
    # call it. Just sleep for a split second.
    # hub.update_cache()
    sleep(0.2)
    assert hub.get_all_service_names() == [
        "sample_alias",
        "default_username/sample_name",
    ]

    service = hub.get(alias="sample_alias")
    actual_service.verify(service)

    service = hub.get(owner="default_username", name="sample_name")
    actual_service.verify(service)

    second_service = VerifiableService(
        owner_name="second_username",
        name="second_service",
        alias="second_service",
        topics=["second_", "the", "topics", "are", "here"],
        desc="second_service_description",
        certified=True,
        public=False,
        uuid="7D5D5A94-F45D-4F44-9B65-BAE13C49AAF4",
        state="BETA",
        config=config,
        readme="second_readme_here",
    )
    registered_services.append(second_service.service)

    actual_service = hub.get(alias="second_service")

    assert actual_service is not None
"""


def test_get_with_name(mocker):
    hub = StoryscriptHub(db_path=tempfile.mkdtemp())
    mocker.patch.object(Service, "select")

    assert hub.get("microservice/redis") is not None

    Service.select().where.assert_called_with(
        (Service.username == "microservice") & (Service.name == "redis")
    )


not_python_fixture = JsonFixtureHelper.load_fixture("not_python_fixture")


def test_service_wrapper(mocker):
    hub = StoryscriptHub(db_path=tempfile.mkdtemp())

    mocker.patch.object(GraphQL, "get_all", return_value=[not_python_fixture])

    mocker.patch.object(ServiceData, "from_dict")

    assert hub.get("microservice/not_python") is not None

    ServiceData.from_dict.assert_called_with(
        data={"service_data": not_python_fixture}
    )


def test_get_with_wrap_service(mocker):
    hub = StoryscriptHub(db_path=tempfile.mkdtemp())

    mocker.patch.object(GraphQL, "get_all", return_value=[not_python_fixture])

    mocker.patch.object(ServiceData, "from_dict")

    assert hub.get("microservice/not_python") is not None

    ServiceData.from_dict.assert_called_with(
        data={"service_data": not_python_fixture}
    )
