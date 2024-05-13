from resume.models import Resume
from company.models import Company


def user_has_resume(request):
    try:
        Resume.objects.get(user=request.user)
        return {"user_has_resume":True}
    except:
        return {"user_has_resume":False}


def yes_resume(request):
    try:
        Resume.objects.get(user=request.user)
        ok = True
        return {'yes_resume':ok}
    except:
        ok = False
        return {'yes_resume':ok}


def yes_company(request):
    try:
        Company.objects.get(user=request.user)
        ok = True
        return {'yes_company':ok}
    except:
        ok = False
        return {'yes_company':ok}