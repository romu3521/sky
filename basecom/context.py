import os
import pathlib
from django.conf import settings


def get_context(request):
    context = {}
    param = ""
    param2 = ""

    path=f"{settings.BASE_DIR}/static/js/umd_main.js"
    path2=f"{settings.BASE_DIR}/static/css/style.css"

    is_file = os.path.isfile(path)
    if is_file:
        param = os.path.getmtime(path)
    else:
        pass

    is_file2 = os.path.isfile(path2)
    if is_file2:
        param2 = os.path.getmtime(path2)
    else:
        pass


    context['fileparam'] =param
    context['fileparam2'] =param2



    return context
