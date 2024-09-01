from django.urls import re_path
from .consumers import AnalyticsConsumer

websocket_url = [
    re_path(r'ws/analytics/$', AnalyticsConsumer.as_asgi()),
]
