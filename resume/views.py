from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from resume import models
# from users.models import User

@login_required
def resume_home(request):
    user_fullname = request.user.get_full_name()
    user_email = request.user.email

    context = {
        'fullname': user_fullname,
        'email': user_email,
    }
    return render(request, 'resume/home.html', context)

@login_required
def create_resume(request):
    schools = models.School.objects.all()
    school_len = len(models.School.objects.all())


    context = {
        'schools': schools,
        'school_len': school_len
    }
    return render(request, "resume/create.html", context)