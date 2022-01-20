from django.urls import re_path
from . import consumers


WebSocket_urlpatterns=[
    re_path(r'ws/socket-server/',consumers.chatconsumer.as_asgi()),
]
