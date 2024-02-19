from django.shortcuts import render
from django.contrib.auth.decorators import login_required




@login_required
def resume_home(request):
    return render(request, 'resume/home.html')

@login_required
def create_resume(request):
    return render(request, "resume/create.html")