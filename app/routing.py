from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from chat import consumer

websocket_urlPattern = [
    path('ws/chat/', consumer.DashConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    # 'http':
    'websocket': AuthMiddlewareStack(URLRouter(websocket_urlPattern))

})
