from django.urls import re_path
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path(r"channeltext/<int:channel_id>", consumers.ChatConsumer.as_asgi()),
    path(r"channelvoice/<int:channel_id>", consumers.ChatConsumer.as_asgi()),
]