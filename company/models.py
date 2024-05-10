from django.db import models
from users.models import User
from django_quill.fields import QuillField
from resume.models import Field, State, District, Resume


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company_user', null=True)
    company_name = models.CharField(null=True, blank=True,max_length=200, verbose_name="نام شرکت یا سازمان")
    image = models.ImageField(upload_to='companies/%Y/%m',verbose_name="عکس")
    company_url = models.URLField(max_length=1000, null=True, blank=True, verbose_name="آدرس اینترنتی")
    field = models.ForeignKey(Field, on_delete=models.CASCADE, verbose_name="حوضه کاری بر اساس رشته های هنرستان")
    about = QuillField(verbose_name="درباره شرکت")
    state = models.ForeignKey(State,on_delete=models.CASCADE, verbose_name="استان محل قرار گیری شرکت")
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="ناحیه قرار گیری شرکت")
    description = QuillField(verbose_name="توضیحات، مزایا و نحوه دوره کارآموزی برای کارآموزان")
    send_resume = models.ManyToManyField(Resume, verbose_name="رزومه های ارسال شده", null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    show_mobile = models.BooleanField(default=True, verbose_name="نمایش شماره تلفن همراه به کارآموزان")
    def __str__(self):
        return self.company_name
    class Meta:
        verbose_name = "شرکت"
        verbose_name_plural = 'شرکت ها'