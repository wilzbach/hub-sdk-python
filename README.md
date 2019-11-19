[![PyPi](https://img.shields.io/pypi/v/story-hub.svg?maxAge=600&style=for-the-badge)](https://pypi.python.org/pypi/story-hub)
[![CircleCI](https://img.shields.io/circleci/project/github/storyscript/hub-sdk-python/master.svg?style=for-the-badge)](https://circleci.com/gh/storyscript/hub-sdk-python)
[![Codecov](https://img.shields.io/codecov/c/github/storyscript/hub-sdk-python.svg?style=for-the-badge)](https://codecov.io/github/storyscript/hub-sdk-python)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg?style=for-the-badge)](https://github.com/storyscript/.github/blob/master/CODE_OF_CONDUCT.md)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)](https://github.com/psf/black)

# hub-sdk-python
A Python SDK to access the Storyscript Hub, which supports caching and more

## Developer

Furthermore, install [pre-commit](https://pre-commit.com/#install) and set up a git hook:

```bash
pip install --user pre-commit
pre-commit install
```

This will ensure that every commit is formatted according to [`black`](https://github.com/psf/black).


## Legacy Usage
```python
from storyhub.sdk.StoryscriptHub import StoryscriptHub

python_service = StoryscriptHub().get("python")

print("Service Name:", python_service.name)
print("UUID:", python_service.service_uuid)
print("Alias:", python_service.alias)
print("Username:", python_service.username)
print("Service Data:", python_service.raw_data)
```

## Advanced Usage
The Storyscript Hub SDK provides the ability to safely access the entire hub service data.
```python
from storyhub.sdk.StoryscriptHub import StoryscriptHub

# tell the hub sdk to utilize the service wrapper
# making it easy to access objects safely
hub = StoryscriptHub(service_wrapper=True)

python_service = StoryscriptHub(service_wrapper=True).get("python")

configuration = python_service.configuration()

print("License Type:", configuration.license().name())
print("Startup Command:", configuration.lifecycle().startup().command())
```
