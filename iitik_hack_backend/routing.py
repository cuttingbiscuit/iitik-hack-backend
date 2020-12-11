from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from api.consumers import TaskNotification

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    path('notifications/', TaskNotification),
                ]
            )
        ),
    ),
})

