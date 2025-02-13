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
from .models import FoContact
import re
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.db.models.functions import Random


class HomeView(TemplateView):
    model = None
    template_name="basecom/home.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, **kwargs):
        context = dict()
        posted = FoPosts.objects.filter(is_public_article=True).order_by("-created_at")
        context.update({
            "subtitle":"| ホーム",
            "posted":posted[0:6],
            "descript":"デモサイト公開中：トップ"
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


        """
        import requests
        url = "https://example.com"
        response = requests.get(url)
        html = response.text
        context.update({
            "a":html
            })
        """



        return render(request, self.template_name, context)


class UrllistView(TemplateView):
    model = None
    template_name="basecom/urllist.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, **kwargs):
        context = dict()
        posted = FoPosts.objects.filter(is_public_article=True).order_by("-created_at")


        context.update({
            "subtitle":"| 活動紹介",
            "posted":posted
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
            "subtitle":f'| プロフィール',
            })

        return render(request, self.template_name, context)





class PostsView(TemplateView):
    model = None
    template_name="basecom/post2.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, **kwargs):
        posted = FoPosts.objects.filter(is_public_article=True,url_name=kwargs["urlstr"])[0]

        context = dict()
        if not posted.is_public_article and not request.user.is_authenticated:

            return redirect("/")

        if not request.session.get(f'viewed_post_{posted.id}', False):
            posted.access_count += 1
            posted.save()
            request.session[f'viewed_post_{posted.id}']=True


        text=posted.post_content.replace('\n', '<br>')
        for size in ['large', 'medium', 'small']:
            text = text.replace(f':{{pic1:{size}}}', f'<img class="{size}" src="/{posted.post_pic}" />')

        for size in ['large', 'medium', 'small']:
            text = text.replace(f':{{pic2:{size}}}', f'<img class="{size}" src="/{posted.post_pic2}" />')

        for size in ['large', 'medium', 'small']:
            text = text.replace(f':{{pic3:{size}}}', f'<img class="{size}" src="/{posted.post_pic3}" />')


        context.update({
            "content":posted,
            "content_post_content":text,
            "descript":posted.post_title
            })

        return render(request, self.template_name, context)



class ContactView(TemplateView):
    model = None
    template_name="basecom/contact.html"

    def get_context_data(self,**kwargs):
         context = super().get_context_data(**kwargs)
         return context

    def post(self, request, **kwargs):

        if not (namevalidation(request.POST["name"]) and contactvalidation(request.POST["contact"])):
            return redirect(request.path)

        try:
            EmailValidator()(request.POST["mail"])
            np = FoContact(
                contact_name=request.POST["name"]
                ,contact_mail=request.POST["mail"]
                ,contact_content=request.POST["contact"]
                ,ip_adress=request.META.get('REMOTE_ADDR')
                )
            np.save()
        except ValidationError:
            return redirect(request.path)
        except Exception as e:
            return redirect(request.path)



        return redirect(request.path)


    def get(self, request, **kwargs):
        context = dict()
        context.update({
            "title":"contact",
            "subtitle":f'| コンタクト',
            })


        return render(request, "basecom/contact.html", context)




def namevalidation(text):
    return True


def contactvalidation(text):
   alph = len(re.findall('[A-Za-z]{1}', text))
   allchara = len(text)

   if alph/allchara > 0.8:
       print("ほぼ英語")
       return False
   




   return True
