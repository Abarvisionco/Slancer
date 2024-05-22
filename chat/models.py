from django.db import models
from resume.models import Resume
from company.models import Company
from users.models import User

class ChatRoom(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="کمپانی یا سازمان")
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, verbose_name="رزومه")
    create_time = models.DateTimeField(auto_now=True)
    last_response = models.CharField(max_length=20, blank=True, verbose_name="آخرین پاسخ")

    def __str__(self) -> str:
        return f"{self.company} - {self.resume}"

    def update_last_response(self, user):
        if user == self.company.user:
            self.last_response = "شرکت یا سازمان پاسخ داده"
        else:
            self.last_response = "کارآموز پاسخ داده"
        self.save()

    class Meta:
        verbose_name = "اتاق"
        verbose_name_plural = "اتاق ها"




class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده")
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, verbose_name="اتاق")
    message = models.TextField(verbose_name="پیغام")
    create_time = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.message
    class Meta:
        verbose_name="پیام"
        verbose_name_plural="پیام ها"
