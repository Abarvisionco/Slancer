from django import forms
from users import models
from users.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['mobile']


class ProfileForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)
        self.fields["email"].widget.attrs['class'] = "form-control form--control pl-3"
        self.fields["email"].widget.attrs['placeholder'] = "ایمیل"
        self.fields["first_name"].widget.attrs['placeholder'] = "نام"
        self.fields["first_name"].widget.attrs['required'] = ""
        self.fields["last_name"].widget.attrs['placeholder'] = "نام خانوادگی"
        self.fields["last_name"].widget.attrs['required'] = ""
        self.fields["first_name"].widget.attrs['class'] = "form-control form--control pl-3"
        self.fields["last_name"].widget.attrs['class'] = "form-control form--control pl-3"
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
