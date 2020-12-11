from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync


class TaskNotification(WebsocketConsumer):

    def connect(self):
        if self.scope["user"].is_anonymos:
            self.close
        else:
            self.group_name = str(self.scope["user"].pk)
            async_to_sync(self.channel_layer.group_add)
            self.accept()
    
    def disconnect(self, close_code):
        self.close()
    

    def notify(self, event):
        self.send(text_data=json.dumps(event["text"]))