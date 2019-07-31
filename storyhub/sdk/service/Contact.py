from storyhub.sdk.service.ServiceObject import ServiceObject


class Contact(ServiceObject):
    """
    This represents contact info contained within @ServiceInfo
    """
    def __init__(self, url, name, email, data):
        super().__init__(data)

        self._url = url
        self._name = name
        self._email = email

    @classmethod
    def from_dict(cls, data):
        contact_ = data["contact"]

        return cls(
            url=contact_.get(
                'url', None
            ),
            name=contact_.get(
                'url', None
            ),
            email=contact_.get(
                'email', None
            ),
            data=data
        )

    def url(self):
        return self._url

    def name(self):
        return self._name

    def email(self):
        return self._email
