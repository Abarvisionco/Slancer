from django.shortcuts import render

# default home page
def home(request):
    return render(request,'main/home.html')