from django.db import models
from django.contrib.auth.models import AbstractUser
from users.usermanager import UserManager
# from resume.models import Resume, School

class User(AbstractUser):
    is_author = models.BooleanField(default=False)
    username = None
    mobile = models.CharField(max_length=11,unique=True,verbose_name="شماره موبایل")
    otp = models.PositiveIntegerField(blank=True,null=True)
    otp_create_time = models.DateTimeField(auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = 'mobile'

    # REQUIRED_FIELDS = ['first_name','last_name']

    backend = 'users.backend.MobileBackend'

    is_admin = models.BooleanField(default=False,verbose_name="وضعیت مدیریت")
    # school = models.ForeignKey(School,on_delete=models.SET_NULL, verbose_name="مدرسه محل مدیریت",null=True,blank=True)
    # resume = models.ForeignKey(Resume,on_delete=models.SET_NULL, verbose_name="رزومه",null=True, blank=True)


