import requests
from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DetailView
from django.contrib.auth.decorators import login_required
from users.forms import ProfileForm
from users.models import User
from users import forms, helper
from django.contrib import messages
from resume import models

# For Logout Users
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def login_view(request):
    form = forms.RegisterForm

    if request.method == "POST":
        # IF USER EXIST:
        try:
            if 'mobile' in request.POST:
                global mobile
                mobile = request.POST.get('mobile')
                user = User.objects.get(mobile=mobile)
                # SENT OTP
                otp = helper.get_random_otp()
                helper.sent_otp(mobile, otp)
                print(otp)
                # SAVE OTP
                user.otp = otp
                user.save()
                # SAVE MOBILE ON SESSION
                request.session['user_mobile'] = user.mobile
                # REDIRECT TO VERIFY PAGE
                return HttpResponseRedirect(reverse('verify'))
        # IF USER DOES NOT EXIST
        except User.DoesNotExist:
            form = forms.RegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                # SENT OTP
                otp = helper.get_random_otp()
                helper.sent_otp(mobile, otp)
                print(otp)
                # SAVE OTP
                user.otp = otp
                user.is_active = False
                user.save()
                # SAVE MOBILE ON SESSION
                request.session['user_mobile'] = user.mobile
                # REDIRECT TO VERIFY PAGE
                return HttpResponseRedirect(reverse('verify'))
    return render(request, 'registration/register.html', {'form': form})


def verify(request):
    mobile = request.session.get('user_mobile')
    user = User.objects.get(mobile=mobile)
    # GET OBJECTS USER FOR VIEW ON VERIFY
    first_name = user.first_name
    last_name = user.last_name
    if request.method == "POST":

        # CHECK OTP TIME
        if not helper.check_otp_expire(user.mobile):
            messages.error(request, "کد اعتبار سنجی منقضی شده. لطفا دوباره تلاش کنید")
            return HttpResponseRedirect(reverse('login'))

        # CHECK OTP
        if user.otp != int(request.POST.get('otp')):
            messages.error(request, "کد اعتبار سنجی اشتباه وارد شده است. لطفا با دقت تلاش کنید")
            return HttpResponseRedirect(reverse('verify'))

        # CHECK FIRST_NAME AND LAST_NAME
        if request.POST.get('first_name') == "" and request.POST.get('last_name') == '':
            messages.error(request, "لطفا نام و نام خانوادگی را وارد کنید")
            return HttpResponseRedirect(reverse('verify'))
        else:
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.save()

        user.is_active = True
        user.save()
        # LOGIN USER
        login(request, user)
        messages.success(request, "ثبت نام و یا ورود انجام شد.👌")
        return HttpResponseRedirect(reverse("profile"))

    context = {
        'mobile': mobile,
        'first_name': first_name,
        'last_name': last_name,
    }

    return render(request, 'registration/verify.html', context)

@login_required
def profile_views(request):
    user = request.user
    if models.Resume.objects.filter(user=user):
        return HttpResponseRedirect(reverse_lazy('resume_home'))
    else:
        return HttpResponseRedirect(reverse_lazy('resume_create'))




# Detail Profile
class Profile(LoginRequiredMixin ,UpdateView, DetailView):
    model = User
    template_name = 'registration/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy("profile")
    success_message = "اطلاعات پروفایل شما با موفقیت بروز رسانی شد."
    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data
    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)
