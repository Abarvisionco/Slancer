from django.shortcuts import render
from company.forms import CompanyForm
from company.models import Company
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
from django.urls import  reverse_lazy
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
    context = {
        'co':company,
        'cos':cos,
    }
    return render(request, 'company/detail.html', context)