from django.contrib import admin
from chat.models import Message, ChatRoom

class MessageAdminView(admin.ModelAdmin):
    list_display = ["author", "chat_room", "create_time", "message"]
    list_filter = ['create_time']
    search_fields = ['message']

class ChatRoomAdminView(admin.ModelAdmin):
    list_display = ['company','resume', 'create_time']
    list_filter = ['create_time']
    list_display_links = ['company', 'resume']

admin.site.register(Message, MessageAdminView)
admin.site.register(ChatRoom, ChatRoomAdminView)