from django.db import models
from django.utils import timezone
from django.db import models
from django_quill.fields import QuillField
from users.models import User


class State(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام استان")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "استان"
        verbose_name_plural = "استان ها"


class City(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام شهر")
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name="استان")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "شهر"
        verbose_name_plural = "شهر ها"


class District(models.Model):
    name = models.CharField(max_length=100, verbose_name="ناحیه")
    city = models.ForeignKey(City, verbose_name="شهر", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.city}"

    class Meta:
        verbose_name = "ناحیه"
        verbose_name_plural = "نواحی"


Gender = (
    ("male", "پسر"),
    ("femal", "دختر")
)


class Field(models.Model):
    name = models.CharField(max_length=20, verbose_name="نام رشته")
    best = models.BooleanField(default=False, verbose_name="محبوب")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "رشته"
        verbose_name_plural = "رشته ها"


class Resume(models.Model):
    '''
        content say something about User have this resume.
        the content can gives image, html codes and ...
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    about = QuillField(null=True)
    school = models.CharField(verbose_name="نام هنرستان", max_length=300, null=True)
    district = models.ForeignKey(District, verbose_name="ناحیه محل هنرستان", on_delete=models.SET_NULL, null=True)
    update_date = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروز رسانی")
    linkedin = models.URLField(verbose_name="آدرس لینکدین", blank=True, null=True)
    link = models.URLField(verbose_name="آدرس سایت", blank=True, null=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, null=True, verbose_name="رشته")
    address = models.TextField(verbose_name="آدرس محل سکونت", blank=True, null=True)
    birth_day = models.IntegerField(verbose_name="روز تولد", blank=True, null=True)
    birth_mount = models.IntegerField(verbose_name="ماه تولد", blank=True, null=True)
    birth_year = models.IntegerField(verbose_name="سال تولد", blank=True, null=True)
    resume_file = models.FileField(verbose_name="فایل رزومه شخصی", upload_to="resume_files/%Y/%m/", blank=True,null=True)
    image = models.ImageField(verbose_name="تصویر", upload_to='resume_images/%Y/%m/', blank=True, null=True)
    create_time = models.DateTimeField(verbose_name="تاریخ ایجاد", auto_now_add=True, null=True)
    active = models.BooleanField(default=True, verbose_name="وضعیت نمایش رزومه به دیگران")

    def __str__(self):
        return f"{self.user.mobile} | {self.user.get_full_name()}"

    class Meta:
        verbose_name = "رزومه"
        verbose_name_plural = "رزومه ها"


class WorkExperience(models.Model):
    name = models.CharField(max_length=100, verbose_name="عنوان شغل")
    co_name = models.CharField(max_length=200, verbose_name="نام سازمان محل فعالیت")
    description = models.TextField(verbose_name="توضیحات")
    start_date = models.DateField(verbose_name="تاریخ شروع")
    end_date = models.DateField(verbose_name="تاریخ پایان", null=True, blank=True)
    resume = models.ForeignKey(Resume, verbose_name="رزومه", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "سابقه شغلی"
        verbose_name_plural = "سوابق شغلی"


Level_CHOICE = (
    ("a", "مقدماتی"),
    ("b", "متوسط"),
    ("c", "پیشرفته")
)


class Skills(models.Model):
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=5, choices=Level_CHOICE, default='a', verbose_name="سطح مهارت")
    resume = models.ForeignKey(Resume, verbose_name="رزومه", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "مهارت"
        verbose_name_plural = "مهارت ها"


class Language(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام زبان")
    level = models.CharField(max_length=5, choices=Level_CHOICE, default='a', verbose_name="سطح زبان")
    resume = models.ForeignKey(Resume, verbose_name="رزومه", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "زبان"
        verbose_name_plural = "زبان ها"


class Courses(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دوره آموزشی")
    description = models.TextField(verbose_name="توشیحات دوره")
    level = models.CharField(max_length=5, choices=Level_CHOICE, default='a', verbose_name="سطح دوره")
    start_date = models.DateField(verbose_name="تاریخ شروع دوره")
    end_date = models.DateField(verbose_name="تاریخ اتمام دوره", null=True, blank=True)
    resume = models.ForeignKey(Resume, verbose_name="رزومه", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دوره آموزشی"
        verbose_name_plural = "دوره های آموزشی"


class ExamWorks(models.Model):
    name = models.CharField(max_length=200, verbose_name="عنوان نمونه کار")
    link = models.URLField(verbose_name="آدرس نمونه کار", null=True, blank=True)
    image = models.ImageField(verbose_name="عکس نمونه کار",null=True, blank=True, upload_to='exam_works/%Y/%m')
    description = models.TextField(verbose_name="توضیحات")
    resume = models.ForeignKey(Resume, verbose_name="رزومه", on_delete=models.CASCADE)
    update_date = models.DateTimeField(null=True, auto_now=True, verbose_name="زمان بروز رسانی")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "نمونه کار"
        verbose_name_plural = "نمونه کار ها"
