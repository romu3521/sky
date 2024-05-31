from django.http import HttpResponse

from django.shortcuts import render
from django.core.paginator import Paginator


from django.db import models
from django.template.response import TemplateResponse
import os
from django.views.generic import TemplateView
from django.shortcuts import redirect

from django.core.exceptions import ObjectDoesNotExist


class HomeView(TemplateView):
    model = None
    template_name="basecom/home.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, **kwargs):
        context = dict()
        context.update({
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


