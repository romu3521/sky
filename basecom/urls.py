from django.urls import path
from .views import HomeView,ProfileView

urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("index.html", HomeView.as_view(), name="index"),
    path("profile.html", ProfileView.as_view(), name="profile"),
]
