from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from chat.models import Message, ChatRoom
from chat.forms import MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def chat(request):
    co = ChatRoom.objects.filter(company__user=request.user)
    resume = ChatRoom.objects.filter(resume__user=request.user)
    
    # get chat room for show
    room = request.GET.get('room_id', '')
    if room and type(room) == int:
        chats = Message.objects.filter(chat_room__id = int(room))
        room_name = ChatRoom.objects.filter(id=id).first()
    else:
        chats = None
        room_name = None

    context = {
        'company':co,
        'resume':resume,
        'chats': chats,
        'room_name': room_name
    }
    return render(request, 'chat/chat.html',context)







@login_required
def send_message(request, chat_room_id):
    chat_room = get_object_or_404(ChatRoom, id=chat_room_id)
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.chat_room = chat_room
            message.save()
            chat_room.update_last_response(request.user)
            messages.success(request, "پیغام شما با موفقیت ارسال شد.")
            return redirect('chat_detail', chat_room_id=chat_room.id)
        else:
            messages.success(request, "ارسال پیام شما با شکست مواجه شد")
            return redirect('chat_detail', chat_room_id=chat_room.id)
        
    else:
        messages.success(request, "ارسال پیام شما با شکست مواجه شد")
        return redirect('chat_detail', chat_room_id=chat_room.id)