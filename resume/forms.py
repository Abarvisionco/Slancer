from django import forms
from resume import models
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime


class ResumeForm(forms.ModelForm):
    class Meta:
        model = models.Resume
        fields = ['about','school','linkedin', 'field','resume_file','address','birth_day','birth_mount','birth_year','active','district','image', 'link']

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
        fields = ['name', 'link', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super(ExamForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control form--control pl-3"

        # اضافه کردن یک توضیح مخصوص برای فرم
        if self.instance.pk:
            self.helper_text = "ویرایش کنید."
        else:
            self.helper_text = "ایجاد کنید."



class WorkForm(forms.ModelForm):
    class Meta:
        model = models.WorkExperience
        fields = ['name', 'co_name', 'description', 'start_date', 'end_date']

    def __init__(self, *args, **kwargs):
        super(WorkForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control form--control pl-3"

        self.fields['start_date'] = JalaliDateField(label=('date'),  # date format is  "yyyy-mm-dd"
                                                    widget=AdminJalaliDateWidget,  # optional, to use default datepicker
                                                    )
        self.fields['end_date'] = JalaliDateField(label=('date1'), widget=AdminJalaliDateWidget,required=False)



class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Courses
        fields = ['name', 'level', 'description', 'start_date', 'end_date']

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control form--control pl-3"

        self.fields['start_date'] = JalaliDateField(label=('date'),  # date format is  "yyyy-mm-dd"
                                                    widget=AdminJalaliDateWidget,  # optional, to use default datepicker
                                                    )
        self.fields['end_date'] = JalaliDateField(label=('date1'), widget=AdminJalaliDateWidget,required=False)

class LangForm(forms.ModelForm):
    class Meta:
        model = models.Language
        fields = ['name','level']

    def __init__(self, *args, **kwargs):
        super(LangForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control form--control pl-3"

        # اضافه کردن یک توضیح مخصوص برای فرم
        if self.instance.pk:
            self.helper_text = "ویرایش کنید."
        else:
            self.helper_text = "ایجاد کنید."


class ResumeFilterForm(forms.ModelForm):
    district = forms.ModelChoiceField(queryset=models.District.objects.all(), empty_label="همه نواحی", label="ناحیه",
                                      required=False)
    state = forms.ModelChoiceField(queryset=models.State.objects.all(), empty_label="همه استان‌ها", label="استان", required=False)
    field = forms.ModelChoiceField(queryset=models.Field.objects.all(),empty_label="همه رشته ها", label=" رشته", required=False)
    # school = forms.ModelChoiceField(queryset=models.Resume.school(), label="نام هنرستان", required=False)
    class Meta:
        model = models.Resume
        fields = ['district', 'field']

    def __init__(self, *args, **kwargs):
        super(ResumeFilterForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control form--control pl-3"

