from django.urls import path
from .views import UrllistView,HomeView,ProfileView,PostsView,SecView
from .models import FoPosts

urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("index.html", HomeView.as_view(), name="index"),
    path("profile.html", ProfileView.as_view(), name="profile"),
    path("post/<urlstr>.html", PostsView.as_view(), name="post"),
    #path("sec.html", SecView.as_view(), name="sec"),
    path("loglist.html", UrllistView.as_view(), name="loglist"),
]
