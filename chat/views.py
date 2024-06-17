from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from chat.models import Message, ChatRoom
from chat.forms import MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from resume.models import Resume
from company.models import Company
from chat.send_message import sent


@login_required
def chat(request):
    form = MessageForm()
    co = ChatRoom.objects.filter(company__user=request.user).order_by("-create_time")
    resume = ChatRoom.objects.filter(resume__user=request.user).order_by("-create_time")
    message_settings = Message.objects.filter(author=request.user)
    sended_messages = message_settings.count()
    last_message_send = message_settings.order_by('-create_time').first()


    # get chat room for show
    room = request.GET.get('room_id', '')
    if room:
        chats = Message.objects.filter(chat_room__id = int(room)).order_by('create_time')
        room_name = ChatRoom.objects.filter(id=int(room)).first()
        try:
            if room_name.company.user != request.user and room_name.resume.user != request.user:
                room_name = None
                chats = None
        except:
            room_name = None
            chats = None
    else:
        chats = None
        room_name = None

    context = {
        'company':co,
        'resume':resume,
        'chats': chats,
        'room_name': room_name,
        'sended_messages': sended_messages,
        "last_message_send":last_message_send,
        'form':form,
    }
    if room:
        context['room'] = int(room)
    return render(request, 'chat/chat.html',context)




@login_required
def delete_chat(request, chat_room_id):
    chat_room = get_object_or_404(ChatRoom, id=chat_room_id)
    redirect_url = reverse('chat')

    try:
        if chat_room.company.user == request.user or chat_room.resume.user == request.user:
            if request.method == "POST":
                chat_room.delete()
                messages.success(request, "چت با موفقیت حذف شد.")
                return redirect(redirect_url)
            else:
                messages.success(request, "حذف چت با شکست مواجه شد")
                return redirect(redirect_url)
            
        else:
            messages.success(request, "شما دسترسی ندارید.")

    except:
        messages.success(request, "حذف چت با شکست مواجه شد")
        return redirect(redirect_url)

    



@login_required
def send_message(request, chat_room_id):
    chat_room = get_object_or_404(ChatRoom, id=chat_room_id)
    redirect_url = reverse('chat') + f'?room_id={chat_room_id}'

    try:
        if chat_room.company.user == request.user or chat_room.resume.user == request.user:
            if request.method == "POST":
                form = MessageForm(request.POST)
                if form.is_valid():
                    message = form.save(commit=False)
                    message.author = request.user
                    message.chat_room = chat_room
                    message.save()
                    if chat_room.company.user == request.user:
                        sent(mobile=chat_room.resume.user.mobile, name=chat_room.resume.user.first_name, yaro=chat_room.company.user.first_name, chat=chat_room_id)
                    else:
                        sent(mobile=chat_room.company.user.mobile, name=chat_room.company.user.first_name, yaro=chat_room.resume.user.first_name, chat=chat_room_id)
                    chat_room.update_last_response(request.user)
                    return redirect(redirect_url)
                else:
                    messages.success(request, "ارسال پیام شما با شکست مواجه شد")
                    return redirect(redirect_url)
            else:
                messages.success(request, "ارسال پیام شما با شکست مواجه شد")
                return redirect(redirect_url)
        else:
            messages.success(request, "شما دسترسی ندارید.")

    except:
        messages.success(request, "ارسال پیام شما با شکست مواجه شد")
        return redirect(redirect_url)


@login_required
def create_room_for_resume(request, id):
    company = get_object_or_404(Company, user__id=id)
    resume = get_object_or_404(Resume, user=request.user)
    if request.method == "POST":
        ChatRoom.objects.create(company=company, resume=resume)
        messages.success(request, f"گفتگو با {company.company_name} ایجاد شد.")
        return redirect(reverse('chat'))
    else:
        messages.error(request, "درخواست نامعتبر است.")
        return redirect(reverse('home'))
    
@login_required
def create_room_for_company(request, id):
    company = get_object_or_404(Company, user=request.user)
    resume = get_object_or_404(Resume, id=id)
    if request.method == "POST":
        ChatRoom.objects.create(company=company, resume=resume)
        messages.success(request, f"گفتگو با {resume.user.get_full_name()} ایجاد شد.")
        return redirect('chat')
    else:
        messages.error(request, "درخواست نامعتبر است.")
        return redirect(reverse('home'))