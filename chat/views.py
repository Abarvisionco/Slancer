# from enum import member
from users.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from chat import models
from resume.models import Resume
from company.models import Company

'''
    login required
    
    this function send user to index chat page
    this page shows to user chat rooms and a input for create chat rooms
    
    basicly this page expired
'''
# @login_required()
# def index(request):
#     # get user
#     user = request.user
#     # get user chatrooms
#     chat_rooms = models.Chat.objects.filter(members = user)
#
#     context = {
#         'chat_rooms':chat_rooms,
#     }
#
#                   NOTE : index.html deleted
#     return render(request, "chat/index.html",context)



# '''
#     index chat room page
    
#     we send room-name chat-model members-list and usernumbers
# '''
# @login_required()
# def room(request, room_name):
#     chat_model = models.Chat.objects.filter(roomname=room_name)

#     if not chat_model.exists():
#         chat = models.Chat.objects.create(roomname=room_name)
#         chat.members.add(request.user)
#     else:
#         chat_model[0].members.add(request.user)

#     members_list =  chat_model[0].members.all()
#     """
#         we send datas to chat room for page
#         after this datas send to back end with user message and save to db.
#     """
#     usernumber = len(members_list)
#     context = {
#         "room_name": room_name,
#         'chat_model': chat_model,
#         'members_list': members_list,
#         'usernumber':usernumber
#     }
#     return render(request, "chat/room.html", context)


@login_required()
def panel(request):

    co = Company.objects.filter(user=request.user)
    resume = Resume.objects.filter(user=request.user)
    context = {
    }
    if co.exists():
        co_chat_rooms = models.Chat.objects.filter(co__in=co)
        context['co_rooms'] = co_chat_rooms
    if resume.exists():
        resume_chat_rooms = models.Chat.objects.filter(user__in=resume)
        context["chat_rooms"] = resume_chat_rooms
    
    return render(request,'panel/panel.html',context)



@login_required()
def room(request, employer_id, jobseeker_id):
    room_name = f"{employer_id}_{jobseeker_id}"
    
    try:
        employer = get_object_or_404(Company, id=employer_id)
        jobseeker = get_object_or_404(Resume, id=jobseeker_id)

        # بررسی اینکه آیا کاربر درخواست دهنده یکی از اعضای مجاز است
        if request.user not in [employer.user, jobseeker.user]:
            if models.Chat.objects.filter(roomname=room_name).exists():
                return HttpResponseForbidden("<center><h2>شما اجازه دسترسی به این اتاق را ندارید.</h2></center>")

        # بررسی اینکه آیا اتاق چت وجود دارد یا خیر
        chat_model, created = models.Chat.objects.get_or_create(roomname=room_name)

        # اگر اتاق تازه ایجاد شده، اعضا را اضافه کنید
        if created:
            chat_model.user(employer.user)
            chat_model.co.add(jobseeker.user)

        # اضافه کردن کاربر فعلی به اعضای اتاق چت
        # chat_model.members.add(request.user)
        # members_list = chat_model.members.all()
        # usernumber = members_list.count()

        context = {
            "room_name": room_name,
            'chat_model': chat_model,
            # 'members_list': members_list,
            # 'usernumber': usernumber
        }
        return render(request, "chat/room.html", context)

    except models.Company.DoesNotExist:
        return HttpResponseNotFound("<center><h2>شرکت پیدا نشد.</h2></center>")
    except models.Resume.DoesNotExist:
        return HttpResponseNotFound("<center><h2>رزومه پیدا نشد.</h2></center>")
    # except Exception as e:
    #     return HttpResponseNotFound(f"<center><h2>خطایی رخ داد: {str(e)}</h2></center>")


'''
    this is new function
    users can delete chat room for her selves
    just chat room never show on user panel
'''
def del_room(request, room_name):
    user = request.user
    cat = models.Chat.objects.get(roomname=room_name)
    cat.members.remove(user)
    return HttpResponseRedirect(reverse_lazy('panel'))

