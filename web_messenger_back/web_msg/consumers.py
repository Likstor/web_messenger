from channels.generic.websocket import AsyncWebsocketConsumer
from app_models.models.channel.channel_text import ChannelText
from app_models.models.message.message import Message
from app_models.models.user.user import User
from app_models.models.server.server import Server
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
		cur_channel_id = self.scope["url_route"]["kwargs"]["channel_id"]
		channel = await sync_to_async(ChannelText.objects.get, thread_sensitive=True)(pk=cur_channel_id)
		current_user = await sync_to_async(User.objects.get, thread_sensitive=True)(pk=text_data_json["user_id"])
		serveruser = await sync_to_async(current_user.serveruser_set.get, thread_sensitive=True)(server_id=channel.server_id)
  
		message = Message(text_channel = channel, 
          user = current_user, 	
          text = text,
          file = None,
          time = datetime.datetime.now())
  
		result = await sync_to_async(message.save, thread_sensitive=True)()
  
		# Send message to room group
		await self.channel_layer.group_send(
			self.room_group_name, {"type": "chat.message", "message": text, "username" : serveruser.username_local, "avatar": str(current_user.avatar)}
		)

	# Receive message from room group
	async def chat_message(self, event):
		# Send message to WebSocket

		print(f"OUT {event}")
		await self.send(text_data=json.dumps({"message": event["message"],
											"username": event["username"],
											"avatar": "/media/" +event["avatar"]}))