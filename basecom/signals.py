from django.conf import settings
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import FoContact
from smtplib import SMTPException



#ディスポーズトークンが作成された時のシグナル
#ディスポーズトークンの情報送信のみ
@receiver(post_save, sender=FoContact)
def publish_resetpass_token(sender, instance, **kwargs):
    if kwargs["created"]:
        title="コンタクト受信のお知らせ"

        print(instance.contact_mail)
        print(instance.contact_name)
        print(instance.ip_adress)
        message=f'''
コンタクト受信
メールアドレス(自称) {instance.contact_mail}
名前(自称)           {instance.contact_name}
IPアドレス           {instance.ip_adress}

'''
        sendmail_user("chro.3521.dyn@gmail.com",title,message)


    return None



def sendmail_user(account_url,subject="",message=""):

    from_email = settings.FROM_EMAIL
    recipient_list = [account_url]
    if settings.MAIL_ENV:
        try:
            send_mail(subject,message,from_email,recipient_list)
        except Exception as e:
            print(e)

            if settings.DEBUG:
             print("to:"+account_url)
             print(f"タイトル{subject}")
             print(message)
    else:

        if settings.DEBUG:
         print("to:"+account_url)
         print(f"タイトル{subject}")
         print(message)






