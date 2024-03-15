from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from resume import models
from resume.forms import ResumeForm, SkillForm
from django.contrib import messages
from django.http import HttpResponseRedirect
# from users.models import User

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
            resume.birth_day = form.cleaned_data['birth_day']
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
    }

    return render(request, 'resume/home.html', context)

def skills(request):
    skills = models.Skills.objects.filter(resume__user=request.user)

    context = {
        'skills': skills,
    }
    return render(request, 'resume/skills/skills.html', context)

def add_skill(request):
    if request.method == "POST":
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                resume = models.Resume.objects.get(user=request.user)
                skills = models.Skills.objects.create(name=form.cleaned_data['name'], level=form.cleaned_data['level'], resume=resume)

                skills.save()
                messages.success(request, f"مهارت {form.cleaned_data['name']} با موفقیت اضافه شد. ")
                return HttpResponseRedirect(reverse_lazy("resume_skills"))
            except:
                messages.error(request, "لطفا اول اطلاعات اولیه رزومه خود را تکمیل کنید")
                return HttpResponseRedirect(reverse_lazy("resume_skills"))
    else:
        form = SkillForm()

    context = {
        'form':form,
        'action': "اضافه",
    }
    return render(request, 'resume/skills/skills_add.html', context)

def delete_skill(request, id):
    try:
        skill = models.Skills.objects.get(id=id, resume__user=request.user)
        messages.success(request,f" {skill} با موفقیت حذف شد. ")
    except:
        messages.error(request,"اعتبار سنجی دچار خطا شد.")
    if request.method == "POST":
        skill.delete()
    return HttpResponseRedirect(reverse_lazy('resume_skills'))

def update_skill(request, id):
    try:
        skill = models.Skills.objects.get(id=id, resume__user=request.user)
        print(skill)
        if request.method == "POST":
            form = SkillForm(request.POST, request.FILES, instance=skill)
            if form.is_valid():
                try:

                    skill.name = form.cleaned_data['name']
                    skill.level = form.cleaned_data['level']
                    skill.save()
                    messages.success(request, f"تغییرات روی {skill.name} با موفقیت اعمال شد. ")
                    return HttpResponseRedirect(reverse_lazy("resume_skills"))
                except:
                    messages.error(request, "هنگام بروز رسانی مشکلی بوجود آمد. لطفا مجدد تلاش کنید.")
                    return HttpResponseRedirect(reverse_lazy("resume_skills"))
        else:
            form = SkillForm(instance=skill)
    except:
        messages.error(request,"اعتبار سنجی دچار خطا شد.")
        return HttpResponseRedirect(reverse_lazy('resume_skills'))

    context = {
        'form':form,
        'action': "ویرایش",
    }
    return render(request, 'resume/skills/skills_add.html', context)

