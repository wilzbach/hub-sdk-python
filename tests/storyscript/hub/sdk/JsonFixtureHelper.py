import json
import os


class JsonFixtureHelper:
    """
    The JsonFixtureHelper just makes it easier to load fixture data from the json_fixture.json file. It's a massive
    blob file with some pre-loaded fixture data.
    """
    _fixture_data = None

    @classmethod
    def load_fixture(cls, name):
        if cls._fixture_data is None:

            dirname = os.path.dirname(__file__)
            path = os.path.join(dirname, "json_fixture.json")

            with open(path, 'r') as f:
                jsonstr = f.read()

                cls._fixture_data = json.loads(jsonstr)

        return cls._fixture_data[name]
