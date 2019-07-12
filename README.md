[![codecov](https://codecov.io/gh/storyscript/hub-sdk-python/branch/master/graph/badge.svg)](https://codecov.io/gh/storyscript/hub-sdk-python)

# hub-sdk-python
A Python SDK to access the Storyscript Hub, which supports caching and more


## Legacy Usage
```python
from storyscript.hub.sdk.StoryscriptHub import StoryscriptHub

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
from storyscript.hub.sdk.StoryscriptHub import StoryscriptHub

# tell the hub sdk to utilize the service wrapper 
# making it easy to access objects safely
hub = StoryscriptHub(service_wrapper=True)

python_service = StoryscriptHub(service_wrapper=True).get("python")

configuration = python_service.configuration()

print("License Type:", configuration.license().name())
print("Startup Command:", configuration.lifecycle().startup().command())
```