from channels.generic.websocket import AsyncWebsocketConsumer
from app_models.models.channel.channel_text import ChannelText
from app_models.models.message.message import Message
from app_models.models.user.user import User
from asgiref.sync import sync_to_async
import datetime
import json

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["channel_id"]
        self.room_group_name = f"chat_{self.room_name}"
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        text = text_data_json["message"]
        print('suka')
        channel = await sync_to_async(ChannelText.objects.get, thread_sensitive=True)(pk=self.scope["url_route"]["kwargs"]["channel_id"])
        current_user = await sync_to_async(User.objects.get, thread_sensitive=True)(pk=text_data_json["user"])
        message = Message(text_channel = channel, 
          user = current_user, 
          text = text,
          file = None,
          time = datetime.datetime.now())
  
        result = await sync_to_async(message.save, thread_sensitive=True)()

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": text}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        print('blyat')
        # Send message to WebSocket"
        await self.send(text_data=json.dumps({"message": message}))