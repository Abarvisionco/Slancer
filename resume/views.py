from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from resume import models
from resume.forms import ResumeForm
# from users.models import User

@login_required
def resume_home(request):
    user_fullname = request.user.get_full_name()
    user_email = request.user.email
    resume = models.Resume.objects.get_or_create(user=request.user)
    form = ResumeForm()
    context = {
        'fullname': user_fullname,
        'email': user_email,
        'resume': resume,
        'form':form,

    }
    return render(request, 'resume/home.html', context)

