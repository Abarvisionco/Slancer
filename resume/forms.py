from django import forms
from resume import models


class ResumeForm(forms.ModelForm):
    class Meta:
        model = models.Resume
        fields = ['about','school','linkedin','resume_file','address','birth_day','birth_mount','birth_year','active','district']

    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)\

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control form--control pl-3"

        # اضافه کردن یک توضیح مخصوص برای فرم
        if self.instance.pk:
            self.helper_text = "ویرایش کنید."
        else:
            self.helper_text = "ایجاد کنید."



class SkillForm(forms.ModelForm):
    class Meta:
        model = models.Skills
        fields = ['name','level']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)\

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control form--control pl-3"

        # اضافه کردن یک توضیح مخصوص برای فرم
        if self.instance.pk:
            self.helper_text = "ویرایش کنید."
        else:
            self.helper_text = "ایجاد کنید."


class ExamForm(forms.ModelForm):
    class Meta:
        model = models.ExamWorks
        fields = ['name', 'link', 'description']

    def __init__(self, *args, **kwargs):
        super(ExamForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control form--control pl-3"

        # اضافه کردن یک توضیح مخصوص برای فرم
        if self.instance.pk:
            self.helper_text = "ویرایش کنید."
        else:
            self.helper_text = "ایجاد کنید."

