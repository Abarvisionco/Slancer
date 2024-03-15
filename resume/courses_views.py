from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from resume.forms import CourseForm
from django.contrib import messages
from resume.models import Courses, Resume
from django.http import HttpResponseRedirect


def home(request):
    exam = Courses.objects.filter(resume__user=request.user)
    context = {
        'exam': exam
    }
    return render(request, 'resume/courses/home.html', context)


def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                resume = Resume.objects.get(user=request.user)
                skills = Courses.objects.create(name=form.cleaned_data['name'],
                                                       level=form.cleaned_data['level'],
                                                       description=form.cleaned_data['description'],
                                                       start_date=form.cleaned_data['start_date'],
                                                       end_date=form.cleaned_data['end_date'], resume=resume)

                skills.save()
                messages.success(request, f" دوره {form.cleaned_data['name']} با موفقیت اضافه شد. ")
                return HttpResponseRedirect(reverse_lazy("courses"))
            except:


                messages.error(request, "لطفا اول اطلاعات اولیه رزومه خود را تکمیل کنید")
                return HttpResponseRedirect(reverse_lazy("courses"))
    else:
        form = CourseForm()

    context = {
        'form': form,
        'action': "اضافه",
    }
    return render(request, 'resume/courses/course_add.html', context)

def update_course(request, id):
    try:
        skill = Courses.objects.get(id=id, resume__user=request.user)
        print(skill)
        if request.method == "POST":
            form = CourseForm(request.POST, request.FILES, instance=skill)
            if form.is_valid():
                try:
                    skill.start_date = form.cleaned_data['start_date']
                    skill.end_date = form.cleaned_data['end_date']
                    skill.description = form.cleaned_data['description']
                    skill.level = form.cleaned_data['level']
                    skill.name = form.cleaned_data['name']
                    skill.save()
                    messages.success(request, f"تغییرات روی {skill.name} با موفقیت اعمال شد. ")
                    return HttpResponseRedirect(reverse_lazy("courses"))
                except:
                    messages.error(request, "هنگام بروز رسانی مشکلی بوجود آمد. لطفا مجدد تلاش کنید.")
                    return HttpResponseRedirect(reverse_lazy("courses"))
        else:
            form = CourseForm(instance=skill)
    except:
        messages.error(request,"اعتبار سنجی دچار خطا شد.")
        return HttpResponseRedirect(reverse_lazy('courses'))

    context = {
        'form':form,
        'action': "ویرایش",
    }
    return render(request, 'resume/courses/course_add.html', context)

def delete_course(request, id):
    try:
        work = Courses.objects.get(id=id, resume__user=request.user)
        messages.success(request,f" {work} با موفقیت حذف شد. ")
    except:
        messages.error(request,"اعتبار سنجی دچار خطا شد.")
    if request.method == "POST":
        work.delete()
    return HttpResponseRedirect(reverse_lazy('courses'))