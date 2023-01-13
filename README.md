<h1 align="center">EndWay Api</h1>
<h4 align="center">https://pypi.org/project/endway-api/</h4>
<p align="center">Library for convenient work with the EndWay forum</p>


<h3 align="center">Installation</h3>

```bash
pip install endway-api
```

-------------------------

<h2 align="center">Get started</h3>
<p align="center">How to start working with the library</p>

```Python
from endway_api import EndWayApi

ewApi = EndWayApi("xf_user")

result = ewApi.add_reply(1, "Hello")
<<<<<<< HEAD
print(result.status_code) # 200
```
--- 
<p align="center">How to get xf_user</p>

* Open forum EndWay
* Open DevTools (F12)
* Open Application
* Open Cookies and select this is site 
* Find xf_user and copy it

-------------------------

<h1 align="center">Documentation</h1>

### Getting a csrf token for later use in requests 
#### You will not need to use this method
```Python
from endway_api import EndWayApi

ewApi = EndWayApi("xf_user")

result = ewApi.get_token()
print(result) # your csrf token
```
| Name         | Type  | Description |
|--------------|-------|-------------|
| `retrun`     | str   | csrf token  |

-------------------------

### Creating a post

```Python
from endway_api import EndWayApi

ewApi = EndWayApi("xf_user")

result = ewApi.post_thread(131, "Test", "Test")
print(result.status_code) # 200
```
| Name         | Type   | Description                                                     |
|--------------|--------|-----------------------------------------------------------------|
| `section_id` | int    | The number of the partition in which the thread will be created |
| `title`      | str    | Topic title                                                     |
| `message`    | str    | Message                                                         |
| `retrun`     | object | Response from the server                                        |

-------------------------

### Sending a message to a thread

```Python
from endway_api import EndWayApi

ewApi = EndWayApi("xf_user")

result = ewApi.add_reply(1236, "Test")
print(result.status_code) # 200
```
| Name        | Type   | Description                                         |
|-------------|--------|-----------------------------------------------------|
| `thread_id` | int    | The thread number to which the message will be sent |
| `message`   | str    | Message                                             |
| `return`    | object | Response from the server                            |

-------------------------

### Creating a post on a user's page

```Python
from endway_api import EndWayApi

ewApi = EndWayApi("xf_user")

result = ewApi.member_post(366, "Test")
print(result.status_code) # 200
```
| Name        | Type       | Description                                                                                                       |
|-------------|------------|-------------------------------------------------------------------------------------------------------------------|
| `member_id` | int or str | Either a permanent user id or a short link. <br/>If permanent id, then type int, if short link, then type string  |
| `message`   | str        | Message                                                                                                           |
| `return`    | object     | Response from the server                                                                                          |

-------------------------

### Creating a comment under a post on a user's page

```Python
from endway_api import EndWayApi

ewApi = EndWayApi("xf_user")

result = ewApi.add_comment(513, "Test")
print(result.status_code) # 200
```
| Name        | Type   | Description                                                                                             |
|-------------|--------|---------------------------------------------------------------------------------------------------------|
| `post_id`   | int    | The number of the message on the user's page<br/>(I do not know how to get it without using DevTools)   |
| `message`   | str    | Message                                                                                                 |
| `return`    | object | Response from the server                                                                                |

-------------------------

### Creating a comment under a post on a user's page

```Python
from endway_api import EndWayApi

ewApi = EndWayApi("xf_user")

result = ewApi.add_comment(513, "Test")
print(result.status_code) # 200
```
| Name        | Type   | Description                                                                                             |
|-------------|--------|---------------------------------------------------------------------------------------------------------|
| `post_id`   | int    | The number of the message on the user's page<br/>(I do not know how to get it without using DevTools)   |
| `message`   | str    | Message                                                                                                 |
| `return`    | object | Response from the server                                                                                |

-------------------------

### Сhanging account information

```Python
from endway_api import EndWayApi

ewApi = EndWayApi("xf_user")

result = ewApi.account_details(location="Test", about_html="Test User")
print(result.status_code) # 200
```
| Name                | Type  | Description                                |
|---------------------|-------|--------------------------------------------|
| `short_link`        | str   | Short link to the page                     |
| `location`          | str   | Place of res idence                        |
| `website`           | str   | Link to your website                       |
| `profilebackground` | str   | Link to the desired background of the page |
| `about_html`        | str   | A brief biography about yourself           |
| `telegram`          | str   | Telegram username without @                |
| `VK`                | str   | Link to VK                                 |
| `steam`             | str   | Link to Steam                              |
| `discord`           | str   | Link to Discord                            |
| `github`            | str   | Link to Dithub                             |
| `return`            | object| Response from the server                   |

-------------------------

### Changing the account password

```Python
from endway_api import EndWayApi

ewApi = EndWayApi("xf_user")

result = ewApi.security("qwerty", "qwerty123")
print(result.status_code) # 200
```
| Name           | Type  | Description                  |
|----------------|-------|------------------------------|
| `old_password` | str   | Old account password         |
| `new_password` | str   | New password for the account |
| `return`       | object| Response from the server     |

-------------------------

### Changing the signature

```Python
from endway_api import EndWayApi

ewApi = EndWayApi("xf_user")

result = ewApi.security("qwerty", "qwerty123")
print(result.status_code) # 200
```
| Name             | Type  | Description             |
|------------------|-------|-------------------------|
| `signature_html` | str   | New signature           |
| `return`         | object| Response from the server|
=======
print(result.status_code)
print(result.json())
```
>>>>>>> ad5da676d3f3799a6af64a410afcf4228e3bdcef
