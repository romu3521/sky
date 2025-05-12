from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template.response import TemplateResponse
from django.shortcuts import render


def hello_blog(request):
    return HttpResponse("Hello Blog!")



class HomeView(TemplateView):
    model = None
    template_name="demosite/home.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, **kwargs):
        context = dict()
#        posted = FoPosts.objects.filter(is_public_article=True).order_by("-created_at")
        context.update({
#            "subtitle":"| ホーム",
#            "posted":posted[0:6],
#            "descript":"デモサイト公開中：トップ"
            })

        return render(request, self.template_name, context)


class Demo1View(TemplateView):
    model = None
    template_name="demosite/demo1.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, **kwargs):
        context = dict()
        context.update({
            })

        return render(request, self.template_name, context)

