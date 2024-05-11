from django.shortcuts import render
from company.forms import CompanyForm
from company.models import Company
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
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
            return HttpResponseRedirect(request.path_info)
    else:
        form = CompanyForm(instance=company)

    context = {
        'form': form,
        'id': request.user.id if request.user.is_authenticated else 0,
    }
    return render(request, 'company/add.html', context)