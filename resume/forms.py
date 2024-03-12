from django import forms
from resume import models


class ResumeForm(forms.ModelForm):
    class Meta:
        model = models.Resume
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__()
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control form--control pl-3"
