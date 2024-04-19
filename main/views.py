from django.shortcuts import render
from resume.models import Field, State, Resume


# default home page
def home(request):
    field = Field.objects.filter(best=True)
    all_field = Field.objects.all()
    state = State.objects.all()
    resume = Resume.objects.order_by("update_date")[:20]
    context = {
        'field':field,
        'all_field':all_field,
        'stete':state,
        'resume':resume,
    }
    return render(request,'main/home.html', context)