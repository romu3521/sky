from django.urls import path
from .views import HomeView,Demo1View

urlpatterns = [
   # path("", HomeView.as_view(), name="index"),
    path("demo1", Demo1View.as_view(), name="demo1"),
]
