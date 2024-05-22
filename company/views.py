from django.shortcuts import render
from company.forms import CompanyForm, CompanyFilterForm
from company.models import Company
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from django.urls import  reverse_lazy, reverse
from resume.models import Resume
from django.core.paginator import Paginator
from chat.models import ChatRoom

@login_required
def company(request):
    company = None
    try:
        company = Company.objects.get(user=request.user)
    except Company.DoesNotExist:
        company = None
    if company == None:
        id = 0
    else:
        id = company.user.id
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            company.save()
            messages.success(request, "تغییرات با موفقیت ذخیره شد.")
            return HttpResponseRedirect(request.path_info)
    else:
        form = CompanyForm(instance=company)

    context = {
        'form': form,
        'id': id
    }
    return render(request, 'company/add.html', context)

def company_detail(request, id):
    company = Company.objects.get(user__id=id)
    cos = Company.objects.order_by('-create_time')[:5]
    resume_ = Resume.objects.order_by('-create_time')[:3]
    send_resume = False
    user_resume = None
    try:
        if resume in company.send_resume.all():
            send_resume = True  
    except:
        pass
    try:
        

        resume = Resume.objects.get(user=request.user)
        chatroom = ChatRoom.objects.filter(company=company)
        print('odk')
        if chatroom.filter(resume=resume):
            print("OK")
            user_resume= True
        else:
            user_resume = resume
        
    except:
        print("NOK")

    context = {
        'co': company,
        'cos': cos,
        'sended_resume': send_resume,
        'resume':resume_,
        'user_resume': user_resume
    }
    return render(request, 'company/detail.html', context)

def add_resume_to_company(request, company_id):
    if request.method == "POST":
        try:
            company = Company.objects.get(user__id=company_id)
            resume = Resume.objects.get(user=request.user)

            if resume in company.send_resume.all():
                company.send_resume.remove(resume)
                messages.success(request, "رزومه با موفقیت از شرکت حذف شد.")
            else:
                company.send_resume.add(resume)
                messages.success(request, "رزومه با موفقیت به شرکت اضافه شد.")

            return HttpResponseRedirect(reverse('co_detail', args=[company_id]))

        except Company.DoesNotExist:
            messages.error(request, "شرکت مورد نظر یافت نشد.")

        except Resume.DoesNotExist:
            messages.error(request, "رزومه کاربر یافت نشد.")

    return HttpResponseRedirect(reverse('co_detail', args=[company_id]))

def company_resume(request):
    company = Company.objects.get(user=request.user)
    paginator = Paginator(company.send_resume.all(), 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'resume':page_obj,
        'id':company.user.id
    }
    return render(request, 'company/company_resume.html', context)

def filter_all_co(request):
    exams = Company.objects.filter()
    form = CompanyFilterForm(request.GET)

    state_query = request.GET.get('state', '')
    if state_query:
        exams = exams.filter(state=state_query)
    district_query = request.GET.get('district', '')
    if district_query:
        exams = exams.filter(district=district_query)
    field_query = request.GET.get('field', '')
    if field_query:
        exams = exams.filter(field=field_query)
    name_query = request.GET.get('name', '')
    if name_query:
        exams = exams.filter(company_name__contains=name_query)

    exams = exams.order_by('-create_time')

    # pagination
    paginator = Paginator(exams, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'exams': page_obj,
        'form':form,
        'resume': page_obj,

    }
    return render(request, 'company/all.html', context)