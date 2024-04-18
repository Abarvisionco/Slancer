from django.shortcuts import render
from resume.models import Field, State


# default home page
def home(request):
    field = Field.objects.filter(best=True)
    all_field = Field.objects.all()
    state = State.objects.all()
    context = {
        'field':field,
        'all_field':all_field,
        'stete':state
    }
    return render(request,'main/home.html', context)