from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from resume.forms import WorkForm
from resume.models import WorkExperience
from django.contrib import messages
from resume.models import Resume
from django.http import HttpResponseRedirect


def home(request):
    exam = WorkExperience.objects.filter(resume__user=request.user)
    context = {
        'exam': exam
    }
    return render(request, 'resume/work/home.html', context)


def add_work(request):
    if request.method == "POST":
        form = WorkForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                resume = Resume.objects.get(user=request.user)
                skills = WorkExperience.objects.create(name=form.cleaned_data['name'],
                                                       co_name=form.cleaned_data['co_name'],
                                                       description=form.cleaned_data['description'],
                                                       start_date=form.cleaned_data['start_date'],
                                                       end_date=form.cleaned_data['end_date'], resume=resume)

                skills.save()
                messages.success(request, f" سابقه شغلی{form.cleaned_data['name']} با موفقیت اضافه شد. ")
                return HttpResponseRedirect(reverse_lazy("work_experience"))
            except:


                messages.error(request, "لطفا اول اطلاعات اولیه رزومه خود را تکمیل کنید")
                return HttpResponseRedirect(reverse_lazy("work_experience"))
    else:
        form = WorkForm()

    context = {
        'form': form,
        'action': "اضافه",
    }
    return render(request, 'resume/work/exam_add.html', context)

def update_work(request, id):
    try:
        skill = WorkExperience.objects.get(id=id, resume__user=request.user)
        print(skill)
        if request.method == "POST":
            form = WorkForm(request.POST, request.FILES, instance=skill)
            if form.is_valid():
                try:
                    skill.start_date = form.cleaned_data['start_date']
                    skill.end_date = form.cleaned_data['end_date']
                    skill.description = form.cleaned_data['description']
                    skill.co_name = form.cleaned_data['co_name']
                    skill.name = form.cleaned_data['name']
                    skill.save()
                    messages.success(request, f"تغییرات روی {skill.name} با موفقیت اعمال شد. ")
                    return HttpResponseRedirect(reverse_lazy("work_experience"))
                except:
                    messages.error(request, "هنگام بروز رسانی مشکلی بوجود آمد. لطفا مجدد تلاش کنید.")
                    return HttpResponseRedirect(reverse_lazy("work_experience"))
        else:
            form = WorkForm(instance=skill)
    except:
        messages.error(request,"اعتبار سنجی دچار خطا شد.")
        return HttpResponseRedirect(reverse_lazy('work_experience'))

    context = {
        'form':form,
        'action': "ویرایش",
    }
    return render(request, 'resume/work/exam_add.html', context)

def delete_work(request, id):
    try:
        work = WorkExperience.objects.get(id=id, resume__user=request.user)
        messages.success(request,f" {work} با موفقیت حذف شد. ")
    except:
        messages.error(request,"اعتبار سنجی دچار خطا شد.")
    if request.method == "POST":
        work.delete()
    return HttpResponseRedirect(reverse_lazy('work_experience'))