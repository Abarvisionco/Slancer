from django.urls import path
from chat import views



urlpatterns = [
    path('', views.chat, name="chat"),
    path('send_resume/<int:chat_room_id>/', views.send_message, name='send_message'),
    path('delte_chat/<int:chat_room_id>/', views.delete_chat, name='delete_chat'),
    path('create_chat/<int:id>/', views.create_room_for_resume, name='create_room_for_user')
]
