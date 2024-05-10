from django.shortcuts import render
from company.forms import CompanyForm
from company.models import Company
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.urls import  reverse_lazy

@login_required
def company(request):
    form = CompanyForm()
    id = 0
    try:
        company = Company.objects.get(user=request.user)
        form = CompanyForm(instance=company)
        id = int(company.user.id)
    except:
        id = 0

    if request.method == 'POST':
        co, created = Company.objects.get_or_create(user=request.user)
        form = CompanyForm(request.POST, request.FILES, instance=co)
        if form.is_valid():
            co.user = request.user
            co.company_name = form.cleaned_data['company_name']
            co.image = form.cleaned_data['image']
            co.company_url = form.cleaned_data['company_url']
            co.field = form.cleaned_data['field']
            co.about = form.cleaned_data['about']
            co.state = form.cleaned_data['state']
            co.district = form.cleaned_data['district']
            co.description = form.cleaned_data['description']
            co.show_mobile = form.cleaned_data['show_mobile']
            form.save()
            return HttpResponseRedirect(reverse_lazy('company'))
    else:
        try:
            co = Company.objects.get(user=request.user)
            form = CompanyForm(instance=co)
            id = request.user.id
        except:
            form = CompanyForm()
            id = 0

    context = {
        'form': form,
        'id': id,
    }
    return render(request, 'company/add.html', context)
