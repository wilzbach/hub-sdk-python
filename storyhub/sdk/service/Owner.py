from storyhub.sdk.service.ServiceObject import ServiceObject


class Owner(ServiceObject):
    def __init__(self, username, data):
        super().__init__(data)

        self._username = username

    @classmethod
    def from_dict(cls, data):
        owner_ = data["owner"]

        return cls(username=owner_.get("username", None), data=data)

    def username(self):
        return self._username
