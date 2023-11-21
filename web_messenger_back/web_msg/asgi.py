from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from .routing import websocket_urlpatterns
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_msg.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
        # Just HTTP for now. (We can add other protocols later.)
    }
)