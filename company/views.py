from django.shortcuts import render
from company.forms import CompanyForm
from company.models import Company
from django.contrib.auth.decorators import login_required


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
        # if form.is_valid():
        #     form.

    context = {
        'form': form,
        'id': id,
    }
    return render(request, 'company/add.html', context)
