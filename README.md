# simple_django_channels

This is a simple example of websockets with django channels.

Try it out by running the following python script:

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
