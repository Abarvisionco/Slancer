import json
from chat.models import Message
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from chat.serializers import MessageSerializer
from rest_framework.renderers import JSONRenderer
from django.contrib.auth import get_user_model
from chat import models

# Get user model
User = get_user_model()

class ChatConsumer(WebsocketConsumer):

    def new_message(self, data):
        message = data['message']
        author = data['username']
        roomname = data['roomname']
        self.notif(data)
        chat_model = models.Chat.objects.get(roomname=roomname)

        user_model = User.objects.filter(mobile=author).first()
        try:
            message_model = Message.objects.create(author=user_model, content=message, related_chat=chat_model, image=user_model.image.url)
        except:
            message_model = Message.objects.create(author=user_model, content=message, related_chat=chat_model, image="/static/images/Sample_User_Icon.png")

        result = self.message_serializer(message_model)
        self.send_to_chat_message(result)

    def notif(self, data):
        message_room_name = data['roomname']
        chat_room_qs = models.Chat.objects.filter(roomname=message_room_name)

        members_list = [i.username for i in chat_room_qs[0].members.all()]

        async_to_sync(self.channel_layer.group_send)(
            'chat_listener',
            {
                '__str__': data['username'],
                "type": "chat.message",
                "content": data['message'],
                'roomname': message_room_name,
                'members_list': members_list,
            })

    def fetch_message(self, data):
        roomname = data['roomname']
        qs = Message.last_messages(self, roomname)

        for i in qs:
            user_image = User.objects.get(username=i.__str__())
            if user_image.image == "":
                i.__dict__.update({"image": "/static/images/Sample_User_Icon.png"})
            else:
                i.__dict__.update({"image": user_image.image})

        message_json = self.message_serializer(qs)

        content = {
            "message": json.loads(message_json),
            'command': "fetch_message",
        }
        self.chat_message(content)

    def image(self, data):
        self.new_message(data)

    def message_serializer(self, qs):
        serialized = MessageSerializer(qs, many=(lambda qs: True if (qs.__class__.__name__ == 'QuerySet') else False)(qs))
        content = JSONRenderer().render(serialized.data)
        return content

    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    commands = {
        "new_message": new_message,
        "fetch_message": fetch_message,
        "img": image,
    }

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        command = text_data_json["command"]
        self.commands[command](self, text_data_json)

    def send_to_chat_message(self, message):
        command = message.get('command', None)
        timestamp = message.get('timestamp', None)
        user_image = User.objects.get(username=message['__str__'])

        try:
            async_to_sync(self.channel_layer.group_send)(self.room_group_name,
                                                         {
                                                             '__str__': message['__str__'],
                                                             'timestamp': timestamp,
                                                             "type": "chat.message",
                                                             "content": message['content'],
                                                             'image': user_image.image.url,
                                                             'command': 'img' if command == 'img' else "new_message",
                                                         })
        except:
            async_to_sync(self.channel_layer.group_send)(self.room_group_name,
                                                         {
                                                             '__str__': message['__str__'],
                                                             'timestamp': timestamp,
                                                             "type": "chat.message",
                                                             "content": message['content'],
                                                             'command': 'img' if command == 'img' else "new_message",
                                                         })

    def chat_message(self, event):
        self.send(text_data=json.dumps(event))