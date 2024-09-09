import os
import pathlib
from django.conf import settings


def get_context(request):
    context = {}
    param = ""
    param2 = ""

    path_t=f"{settings.BASE_DIR}/static/css"
    param_t = os.path.getmtime(path_t)


    path_js=f"{settings.BASE_DIR}/static/js"
    param_js = os.path.getmtime(path_js)


    context['fileparam'] =param_t
    context['fileparam2'] =param_t
    context['fileparamjs'] =param_js
    context['descript'] ="デモサイト稼働！"
    context['host'] =request.get_host()



    return context
