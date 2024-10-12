from django.urls import path
from .consumer import GraphConsumer

ws_urlpatterns = [
    path("ws/jcdecaux/", GraphConsumer.as_asgi())
]