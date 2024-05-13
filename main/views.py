from django.shortcuts import render
from resume.models import Field, State, Resume, ExamWorks
from company.models import Company

# default home page
def home(request):
    field = Field.objects.filter(best=True)
    all_field = Field.objects.all()
    state = State.objects.all()
    resume = Resume.objects.order_by("-update_date").filter(active=True)[:12]
    company = Company.objects.order_by("-create_time")[:12]
    context = {
        'field':field,
        'all_field':all_field,
        'stete':state,
        'resume':resume,
        'company':company
    }
    return render(request,'main/home.html', context)

def about(request):
    return render(request, 'main/about.html')


