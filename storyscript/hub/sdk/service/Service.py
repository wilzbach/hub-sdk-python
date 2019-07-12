from storyscript.hub.sdk.service.Owner import Owner
from storyscript.hub.sdk.service.ServiceObject import ServiceObject


class Service(ServiceObject):
    """
    This represents the "service" data stored within the hub.
    """

    def __init__(self, name, alias, owner, certified, public, topics, description, data):
        super().__init__(data)

        self._name = name
        self._alias = alias
        self._owner = owner
        self._certified = certified
        self._public = public
        self._topics = topics
        self._description = description

    @classmethod
    def from_dict(cls, data):
        service = data["service"]

        return cls(
            name=service['name'],
            alias=service['alias'],
            owner=Owner.from_dict(data={
                "owner": service['owner']
            }),
            certified=service["isCertified"],
            public=service["public"],
            topics=service["topics"],
            description=service['description'],
            data=data
        )

    def name(self):
        return self._name

    def alias(self):
        return self._alias

    def owner(self):
        return self._owner

    def description(self):
        return self._description

    def certified(self):
        return self._certified

    def public(self):
        return self._public