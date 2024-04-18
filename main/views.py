from django.shortcuts import render
from resume.models import Field


# default home page
def home(request):
    field = Field.objects.filter(best=True)
    context = {
        'field':field
    }
    return render(request,'main/home.html', context)