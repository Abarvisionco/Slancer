from django.shortcuts import render
from company.forms import CompanyForm
from company.models import Company
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from django.urls import  reverse_lazy, reverse
from resume.models import Resume


@login_required
def company(request):
    try:
        company = Company.objects.get(user=request.user)
    except Company.DoesNotExist:
        company = None

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
        'id': request.user.id if request.user.is_authenticated else 0,
    }
    return render(request, 'company/add.html', context)

def company_detail(request, id):
    company = Company.objects.get(user__id=id)
    cos = Company.objects.order_by('-create_time')[:5]
    send_resume = False
    try:
        resume = Resume.objects.get(user=request.user)
        if resume in company.send_resume.all():
            send_resume = True
        print(send_resume)
    except Resume.DoesNotExist:
        pass

    context = {
        'co': company,
        'cos': cos,
        'sended_resume': send_resume
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