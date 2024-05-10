from django import forms
from company import models

class CompanyForm(forms.ModelForm):
    class Meta:
        model = models.Company
        fields = ['company_name', 'image', 'company_url', 'field', 'about', 'state', 'district', 'description', 'show_mobile']

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)\

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control form--control pl-3 mb-3"

        # اضافه کردن یک توضیح مخصوص برای فرم
        if self.instance.pk:
            self.helper_text = "ویرایش کنید."
        else:
            self.helper_text = "ایجاد کنید."
