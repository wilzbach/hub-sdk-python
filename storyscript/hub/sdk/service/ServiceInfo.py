from storyscript.hub.sdk.service.Argument import Argument
from storyscript.hub.sdk.service.Contact import Contact
from storyscript.hub.sdk.service.License import License
from storyscript.hub.sdk.service.ServiceObject import ServiceObject

bullshit = {
    "info": {
        "title": "Stockbroker",
        "license": {
            "url": "https://opensource.org/licenses/MIT",
            "name": "MIT"
        },
        "version": "0.0.1",
        "description": "An http service to fetch stock prices",
        "contact": {
            "url": "https://github.com/heaptracetechnology/dropbox-microservice",
            "name": "Rohit Shetty",
            "email": "rohits@heaptrace.com"
        }
    }}


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

        _license = None

        if 'license' in service_info:
            _license = License.from_dict(data={
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
            license_=_license,
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
