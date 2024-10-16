from channels.generic.websocket import WebsocketConsumer
import json
from time import sleep
from random import randint

class GraphConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(1000):
            self.send(json.dumps({"value": randint(-20, 20)}))
            sleep(1)