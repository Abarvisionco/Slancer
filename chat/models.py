from django.db import models
from django.contrib.auth import get_user_model
from resume.models import Resume
from company.models import Company

# User Authenticated
User = get_user_model()

# Create Model Chat
'''
    chat models have a room name for get message from were room
    members can only be viewed once
    create time for show to user when message is send
'''
class Chat(models.Model):
    roomname = models.CharField(max_length=75,blank=True, verbose_name="نام اتاق")
    # members = models.ManyToManyField(User, null=True,blank=True, verbose_name="کاربران")
    co = models.ForeignKey(Company, verbose_name="شرکت", null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(Resume, verbose_name="کاربر", null=True,on_delete=models.CASCADE)
    createtime = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    def __str__(self):
        return str(self.roomname)
    class Meta:
        verbose_name = "اتاق"
        verbose_name_plural = "اتاق ها"




# Create Model Message
'''
    every message have one chat.
    every message have one author.
    every message have content ( this content maybe base64 image or text )
    every message have an image ( this image save from author image )
'''
class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="سازنده")
    content = models.TextField(verbose_name="پیام")
    related_chat = models.ForeignKey(Chat, on_delete=models.CASCADE,blank=True,null=True, verbose_name="چت روم")
    timestamp = models.DateTimeField(auto_now_add=True , verbose_name="تاریخ ایجاد")
    image = models.CharField(max_length=500, blank=True,null=True, verbose_name="عکس")

    def last_messages(self, roomname):
        return Message.objects.filter(related_chat__roomname = roomname).order_by('-timestamp').all()

    def __str__(self):
        return str(self.author)
    
    class Meta:
        verbose_name_plural = "پیام ها"
        verbose_name = "پیام"