from django.urls import path
from linechat.views import line_webhook

urlpatterns = [
    path('webhook/', line_webhook, name='line_webhook'),
]
