from django.db import models
import datetime
from django.db.models import Sum
from django.utils.safestring import mark_safe
import string
from django.utils import timezone
from django.conf import settings
import random
import re
import uuid
import os
import hashlib

if settings.DEBUG:
    imgpath="static/"
else:
    #ここが参照ディレクトリ
    imgpath="static/media"

def get_upload_to(instance, filename):
    # ファイル名をハッシュ化
    hash_name = hashlib.sha1(filename.encode('utf-8')).hexdigest()[:20]
    ext = os.path.splitext(filename)[1]
    return f'{imgpath}/{hash_name}{ext}'


class FoContact(models.Model):
    contact_content = models.TextField(default="", blank=True, null=True)
    contact_mail = models.CharField(max_length=100, blank=True, null=True)
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now,blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now,blank=True, null=True)
    ip_adress = models.CharField(max_length=50,default="", blank=True, null=True)
    def __str__(self):
        return str(self.created_at)+"　　"+str(self.contact_mail)
    class Meta:
        verbose_name_plural = "コンタクト"



class FoPosts(models.Model):
    id = models.AutoField(primary_key=True)
    url_name = models.CharField(verbose_name="url文字列",max_length=100, blank=True, null=True,unique=True)
    redirect_url = models.CharField(max_length=50, blank=True, null=True)
    post_title = models.TextField(verbose_name="記事タイトル",default="", blank=True, null=True)
    post_content = models.TextField(default="", blank=True, null=True)
    author_name = models.CharField(verbose_name="著者名",max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now,blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now,blank=True, null=True)
    access_count = models.PositiveBigIntegerField(default=0, blank=True, null=True)
    post_pic = models.ImageField(upload_to=get_upload_to, null=True,blank=True)
    post_pic2 = models.ImageField(upload_to=get_upload_to, null=True,blank=True)
    post_pic3 = models.ImageField(upload_to=get_upload_to, null=True,blank=True)
    post_pic4 = models.ImageField(upload_to=get_upload_to, null=True,blank=True)
    post_pic5 = models.ImageField(upload_to=get_upload_to, null=True,blank=True)
    #parent_genre = models.ForeignKey(FoGenres, on_delete=models.SET_DEFAULT,default=None, null=False)
    is_public_article = models.BooleanField(verbose_name="記事を公開する",default=False)
    is_public_cmt = models.BooleanField(verbose_name="コメント公開する",default=False)
    #tags = models.ManyToManyField("FoTags", related_name='posts',blank=True)
    cite = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.url_name:
            self.url_name = datetime.date.today().strftime("%Y%m%d")+''.join(random.choices(string.ascii_letters, k=4))
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.post_title[:20])+"..."
    def get_tags(self):
        return self.tags.all()
    def get_description_summary(self):
        clean = re.compile('<.*?>')
        cleaned = re.sub(clean, '', self.post_content)
        clean = re.compile(':{.*?}')
        cleaned = re.sub(clean, '', cleaned)
        return cleaned[:70]
    class Meta:
        verbose_name_plural = "投稿"




class FoComments(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment_content = models.TextField(default="", blank=True, null=True)
    display_authorname = models.TextField(default=None, blank=True, null=True)
    contact_mail = models.CharField(max_length=100, blank=True, null=True)
    parent_post = models.ForeignKey(FoPosts, on_delete=models.CASCADE, blank=True, null=True)
    ip_adress = models.CharField(max_length=50,default="", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now,blank=True, null=True)

    def __str__(self):
        return str(self.created_at)+"　　"+self.comment_content[0:20]
    class Meta:
        verbose_name_plural = "投稿コメント"




