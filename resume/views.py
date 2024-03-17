from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from resume import models
from resume.forms import ResumeForm
from django.http import HttpResponseRedirect

@login_required
def resume_home(request):
    user_fullname = request.user.get_full_name()
    user_email = request.user.email
    resume, created = models.Resume.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES, instance=resume)
        if form.is_valid():
            # بروزرسانی مقادیر فیلدهای مربوط به Resume با داده‌های ورودی فرم
            resume.school = form.cleaned_data['school']
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
        form = ResumeForm(instance=resume)

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
    context = {
        'resume':resume,
        'langs':langs,
        'skills':skills,
        'exams':exams,
    }
    return render(request, 'resume/resume.html', context)
