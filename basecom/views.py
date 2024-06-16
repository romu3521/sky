from django.http import HttpResponse

from django.shortcuts import render
from django.core.paginator import Paginator


from django.db import models
from django.template.response import TemplateResponse
import os
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .models import FoPosts

from django.core.exceptions import ObjectDoesNotExist


class HomeView(TemplateView):
    model = None
    template_name="basecom/home.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, **kwargs):
        context = dict()
        posted = FoPosts.objects.filter().order_by("-created_at")
        context.update({
            "posted":posted[0:6]
            })

        return render(request, self.template_name, context)

class SecView(TemplateView):
    model = None
    template_name="basecom/secret.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, **kwargs):
        context = dict()


        import requests
        url = "https://example.com"
        response = requests.get(url)
        html = response.text
        context.update({
            "a":html
            })



        return render(request, self.template_name, context)




class ProfileView(TemplateView):
    model = None
    template_name="basecom/profile.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, **kwargs):
        context = dict()
        context.update({
            })

        return render(request, self.template_name, context)


class PostsView(TemplateView):
    model = None
    template_name="basecom/post.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, **kwargs):

        posted = FoPosts.objects.filter(url_name=kwargs["urlstr"])[0]
        context = dict()
        context.update({
            "content":posted,
            "content_post_content":posted.post_content.replace('\n', '<br>')
            })

        return render(request, self.template_name, context)


