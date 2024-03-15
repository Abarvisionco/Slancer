from resume import models
from resume.forms import ResumeForm, SkillForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render

def skills(request):
    skills = models.Skills.objects.filter(resume__user=request.user)
    id = models.Resume.objects.get(user=request.user).id
    context = {
        'skills': skills,
        'id':id,
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
