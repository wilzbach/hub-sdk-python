from storyhub.sdk.service.Contact import Contact
from storyhub.sdk.service.License import License
from storyhub.sdk.service.ServiceObject import ServiceObject


class ServiceInfo(ServiceObject):

    def __init__(self, title, license_, version, description, contact, data):
        super().__init__(data)

        self._title = title
        self._license = license_
        self._version = version
        self._description = description
        self._contact = contact

    @classmethod
    def from_dict(cls, data):
        service_info = data["service_info"]

        license_ = None

        if 'license' in service_info:
            license_ = License.from_dict(data={
                "license": service_info["license"]
            })

        contact = None

        if 'contact' in service_info:
            contact = Contact.from_dict(data={
                "contact": service_info["contact"]
            })

        return cls(
            title=service_info.get(
                "title", None
            ),
            license_=license_,
            version=service_info.get(
                "version", None
            ),
            description=service_info.get(
                "description", None
            ),
            contact=contact,
            data=data
        )

    def title(self):
        return self._title

    def license(self):
        return self._license

    def version(self):
        return self._version

    def description(self):
        return self._description

    def contact(self):
        return self._contact
