from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from resume.forms import ExamForm
from resume.models import ExamWorks, Resume
from django.http import HttpResponseRedirect

def home(request):
    resume = Resume.objects.get(user=request.user)
    exam = ExamWorks.objects.filter(resume__user=request.user)
    context = {
        'exam':exam,
        'id':resume.id,
    }
    return render(request,'resume/exam/home.html', context)

def add_exam(request):
    if request.method == "POST":
        form = ExamForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                resume = Resume.objects.get(user=request.user)
                skills = ExamWorks.objects.create(name=form.cleaned_data['name'], link=form.cleaned_data['link'], description=form.cleaned_data['description'], resume=resume)

                skills.save()
                messages.success(request, f"نمونه کار {form.cleaned_data['name']} با موفقیت اضافه شد. ")
                return HttpResponseRedirect(reverse_lazy("exam"))
            except:
                messages.error(request, "لطفا اول اطلاعات اولیه رزومه خود را تکمیل کنید")
                return HttpResponseRedirect(reverse_lazy("exam"))
    else:
        form = ExamForm()

    context = {
        'form':form,
        'action': "اضافه",
    }
    return render(request, 'resume/exam/exam_add.html', context)

def update_exam(request, id):
    try:
        skill = ExamWorks.objects.get(id=id, resume__user=request.user)
        print(skill)
        if request.method == "POST":
            form = ExamForm(request.POST, request.FILES, instance=skill)
            if form.is_valid():
                try:

                    skill.name = form.cleaned_data['name']
                    skill.level = form.cleaned_data['link']
                    skill.description = form.cleaned_data['description']
                    skill.save()
                    messages.success(request, f"تغییرات روی {skill.name} با موفقیت اعمال شد. ")
                    return HttpResponseRedirect(reverse_lazy("exam"))
                except:
                    messages.error(request, "هنگام بروز رسانی مشکلی بوجود آمد. لطفا مجدد تلاش کنید.")
                    return HttpResponseRedirect(reverse_lazy("exam"))
        else:
            form = ExamForm(instance=skill)
    except:
        messages.error(request,"اعتبار سنجی دچار خطا شد.")
        return HttpResponseRedirect(reverse_lazy('exam'))

    context = {
        'form':form,
        'action': "ویرایش",
    }
    return render(request, 'resume/exam/exam_add.html', context)


def delete_exam(request, id):
    try:
        skill = ExamWorks.objects.get(id=id, resume__user=request.user)
        messages.success(request,f" {skill} با موفقیت حذف شد. ")
    except:
        messages.error(request,"اعتبار سنجی دچار خطا شد.")
    if request.method == "POST":
        skill.delete()
    return HttpResponseRedirect(reverse_lazy('exam'))