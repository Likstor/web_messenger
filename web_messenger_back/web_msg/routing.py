from django.urls import re_path
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path(r"channel/<int:channel_id>", consumers.ChatConsumer.as_asgi()),
]