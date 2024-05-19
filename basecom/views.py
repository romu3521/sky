from django.http import HttpResponse

from django.shortcuts import render
from django.core.paginator import Paginator


from django.db import models
from django.template.response import TemplateResponse
import os
from django.views.generic import TemplateView
from django.shortcuts import redirect

from django.core.exceptions import ObjectDoesNotExist



def index(request):
        context = dict()
        context.update({
            })

        return render(request, "basecom/home.html", context)

