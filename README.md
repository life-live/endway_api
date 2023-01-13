# EndWay Api

Library for convenient work with the EndWay forum

### Installation

```Python
pip
install
endwayapi
```

### Get started

How to start working with the library

```Python
from endway_api import EndWayApi

# Instantiate a EndWayApi object
ewApi = EndWayApi("xf_user")

# call the method of sending a message to the thread
result = ewApi.add_reply(1, "Hello")
print(result.status_code)
print(result.json())
```