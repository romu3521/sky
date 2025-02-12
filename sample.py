from django.core.mail import send_mail
from django.conf import settings


send_mail(
    subject="テストメール",
    message="Django のシェルから送信しました。",
    from_email="",  # 送信元
    recipient_list=["chro.3521.dyn@gmail.com"],  # 受信者リスト
    fail_silently=False,  # エラー時に例外を出す
)
