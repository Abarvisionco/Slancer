from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from resume import models
from resume.forms import ResumeForm, ResumeFilterForm
from django.http import HttpResponseRedirect
from chat.models import ChatRoom
from company.models import Company

class ResumeModel:
    def __init__(self, id):
        self.id = id

@login_required
def resume_home(request):
    user_fullname = request.user.get_full_name()
    user_email = request.user.email
    form = ResumeForm()
    if request.method == "POST":
        resume, created = models.Resume.objects.get_or_create(user=request.user)
        form = ResumeForm(request.POST, request.FILES, instance=resume)
        if form.is_valid():
            # بروزرسانی مقادیر فیلدهای مربوط به Resume با داده‌های ورودی فرم
            resume.school = form.cleaned_data['school']
            resume.field = form.cleaned_data['field']
            resume.linkedin = form.cleaned_data['linkedin']
            resume.resume_file = form.cleaned_data['resume_file']
            resume.image = form.cleaned_data['image']
            resume.birth_day = form.cleaned_data['birth_day']
            resume.link = form.cleaned_data['link']
            resume.birth_mount = form.cleaned_data['birth_mount']
            resume.birth_year = form.cleaned_data['birth_year']
            resume.address = form.cleaned_data['address']
            resume.active = form.cleaned_data['active']
            resume.district = form.cleaned_data['district']
            # به‌روزرسانی فیلد user
            resume.user = request.user
            # ذخیره تغییرات در دیتابیس
            # resume_file = form.cleaned_data['resume_file']
            # resume.resume_file.save(resume_file.name, resume_file, save=False)

            resume.save()
            return HttpResponseRedirect(request.path_info)
    else:
        try:
            resume = models.Resume.objects.get(user=request.user)
            form = ResumeForm(instance=resume)
        except:
            resume = ResumeModel(0)

    context = {
        'fullname': user_fullname,
        'email': user_email,
        'resume': resume,
        'form': form,
        'id':resume.id,
    }

    return render(request, 'resume/home.html', context)



def resume(request, id):
    resume = models.Resume.objects.get(id=id)
    langs = models.Language.objects.filter(resume=resume)
    skills = models.Skills.objects.filter(resume=resume)
    exams = models.ExamWorks.objects.filter(resume=resume)
    work = models.WorkExperience.objects.filter(resume=resume)
    course = models.Courses.objects.filter(resume=resume)
    context = {
        'resume':resume,
        'langs':langs,
        'skills':skills,
        'exams':exams,
        'work':work,
        'course':course,
    }
    
    try:
        company = Company.objects.get(user=request.user)
        chatroom = ChatRoom.objects.filter(resume=resume, company=company)
        if chatroom.exists():
            chat = 'no'
        else:
            chat = company

        context['chat'] = chat
    except Company.DoesNotExist:
        context['chat'] = None
        # messages.error(request, "شما هیچ شرکتی ندارید.")

    return render(request, 'resume/resume.html', context)


def filter_resumes(request):
    resume = models.Resume.objects.all().filter(active=True)
    form = ResumeFilterForm(request.GET)
    state_query = request.GET.get('state', '')
    if state_query:
        resume = resume.filter(district__city__state=state_query)
    district_query = request.GET.get('district', '')
    if district_query:
        resume = resume.filter(district=district_query)
    field_query = request.GET.get('field', '')
    if field_query:
        resume = resume.filter(field=field_query)
    name_query = request.GET.get('name', '')
    if name_query:
        resume = resume.filter(school__contains=name_query)

    resume = resume.order_by('-update_date')

    # pagination
    paginator = Paginator(resume, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'resume': page_obj,
        'form':form
    }
    return render(request, 'resume/all_resume.html', context)

def filter_all_exams(request):
    exams = models.ExamWorks.objects.filter(resume__active=True)
    form = ResumeFilterForm(request.GET)

    state_query = request.GET.get('state', '')
    if state_query:
        exams = exams.filter(resume__district__city__state=state_query)
    district_query = request.GET.get('district', '')
    if district_query:
        exams = exams.filter(resume__district=district_query)
    field_query = request.GET.get('field', '')
    if field_query:
        exams = exams.filter(resume__field=field_query)
    name_query = request.GET.get('name', '')
    if name_query:
        exams = exams.filter(resume__school__contains=name_query)

    exams = exams.order_by('-resume__update_date')

    # pagination
    paginator = Paginator(exams, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'exams': page_obj,
        'form':form,
        'resume': page_obj,

    }
    return render(request, 'resume/all_exams.html', context)