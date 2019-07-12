from storyscript.hub.sdk.service.ServiceObject import ServiceObject


class License(ServiceObject):

    def __init__(self, url, name, data):
        super().__init__(data)

        self._url = url
        self._name = name

    @classmethod
    def from_dict(cls, data):
        license_ = data["license"]

        return cls(
            url=license_.get(
                'url', None
            ),
            name=license_.get(
                'name', None
            ),
            data=data
        )

    def url(self):
        return self._url

    def name(self):
        return self._name
