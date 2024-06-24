from django.db import models
from django.utils import timezone
from django.conf import settings
import re

if settings.DEBUG:
    imgpath="static/"
else:
    imgpath="media/"


class FoContact(models.Model):
    contact_content = models.TextField(default="", blank=True, null=True)
    contact_mail = models.CharField(max_length=100, blank=True, null=True)
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now,blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now,blank=True, null=True)
    ip_adress = models.CharField(max_length=50,default="", blank=True, null=True)
    post_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="account", on_delete=models.SET_NULL, null=True,blank=True)
    def __str__(self):
        return str(self.created_at)+"　　"+str(self.contact_mail)
    class Meta:
        verbose_name_plural = "コンタクト"



class FoPosts(models.Model):
    id = models.AutoField(primary_key=True)
    url_name = models.CharField(max_length=100, blank=True, null=True)
    post_title = models.TextField(default="", blank=True, null=True)
    post_content = models.TextField(default="", blank=True, null=True)
    author_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now,blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now,blank=True, null=True)
    access_count = models.PositiveBigIntegerField(default=0, blank=True, null=True)
    post_pic = models.ImageField(upload_to=imgpath, null=True,blank=True)
    post_pic2 = models.ImageField(upload_to=imgpath, null=True,blank=True)
    post_pic3 = models.ImageField(upload_to=imgpath, null=True,blank=True)
    def __str__(self):
        return str(self.created_at)+"　　"+self.post_title
    def get_description_summary(self):
        clean = re.compile('<.*?>')
        cleaned = re.sub(clean, '', self.post_content)
        return cleaned[:160]
    class Meta:
        verbose_name_plural = "投稿"

