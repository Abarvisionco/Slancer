from django import forms
from company.models import Company
from resume import models

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'image', 'company_url', 'field', 'about', 'state', 'district', 'address', 'description', 'show_mobile']

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)\

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control form--control pl-3 mb-3"

        # اضافه کردن یک توضیح مخصوص برای فرم
        if self.instance.pk:
            self.helper_text = "ویرایش کنید."
        else:
            self.helper_text = "ایجاد کنید."


class CompanyFilterForm(forms.ModelForm):
    district = forms.ModelChoiceField(queryset=models.District.objects.all(), empty_label="همه نواحی", label="ناحیه",
                                      required=False)
    state = forms.ModelChoiceField(queryset=models.State.objects.all(), empty_label="همه استان‌ها", label="استان", required=False)
    field = forms.ModelChoiceField(queryset=models.Field.objects.all(),empty_label="همه رشته ها", label=" رشته", required=False)
    # school = forms.ModelChoiceField(queryset=models.Resume.school(), label="نام هنرستان", required=False)
    class Meta:
        model = models.Resume
        fields = ['district', 'field']

    def __init__(self, *args, **kwargs):
        super(CompanyFilterForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control form--control pl-3"

