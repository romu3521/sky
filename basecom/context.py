import os
import pathlib
from django.conf import settings


def get_context(request):
    context = {}
    param = ""

    path=f"{settings.BASE_DIR}/static/js/umd_main.js"
    is_file = os.path.isfile(path)
    if is_file:
        param = os.path.getmtime(path)
    else:
        context['fileparam'] =param



    return context
