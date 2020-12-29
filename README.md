# simple_django_channels

This is a simple example of websockets with django channels.

Test it with following python code:

```
import json
import requests
import redis
import websocket
import random
import time

ws = websocket.WebSocket()

ws.connect('ws://localhost:8000/ws/chat/')

for i in range(1000):
    time.sleep(6)
    ws.send(json.dumps({'message': random.randint(1, 100)}))
    
```

Please give it a star if you found it useful.
