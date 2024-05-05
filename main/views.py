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


def filter_resumes(request):
    resume = Resume.objects.all()

    state_query = request.GET.get('state', '')
    if state_query:
        resume = resume.filter(state=state_query)

    field_query = request.GET.get('field', '')
    if field_query:
        resume = resume.filter(field=field_query)

    name_query = request.GET.get('q', '')
    if name_query:
        resume = resume.filter(name__exact=name_query)

    resume = resume.order_by('update_date')
    # نا تمام
    # return render(request, 'main/home.html', {'resume_list': resume})