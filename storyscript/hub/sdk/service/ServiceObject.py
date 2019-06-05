import json


class ServiceObject:

    def __init__(self, data):
        self._data = data

    @staticmethod
    def _json_to_dict(jsonstr):
        return json.loads(jsonstr)

    @classmethod
    def from_dict(cls, data):
        return cls(
            data=data
        )

    @classmethod
    def from_json(cls, jsonstr):
        return cls.from_dict(data=ServiceObject._json_to_dict(jsonstr=jsonstr))

    def as_json(self, compact=False):
        if compact:
            return json.dumps(self._data, sort_keys=True)

        return json.dumps(self._data, indent=4, sort_keys=True)

    def raw_data(self):
        return self._data.copy()
