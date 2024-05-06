from django.shortcuts import render
from resume.models import Field, State, Resume, ExamWorks


# default home page
def home(request):
    field = Field.objects.filter(best=True)
    all_field = Field.objects.all()
    state = State.objects.all()
    resume = Resume.objects.order_by("-update_date").filter(active=True)[:12]
    exams = ExamWorks.objects.order_by("-update_date")[:16]
    context = {
        'field':field,
        'all_field':all_field,
        'stete':state,
        'resume':resume,
        'exams': exams
    }
    return render(request,'main/home.html', context)

def about(request):
    return render(request, 'main/about.html')


