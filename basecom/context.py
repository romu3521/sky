import os
import pathlib
from django.conf import settings


def get_context(request):
    context = {}
    param = ""
    param2 = ""

    path_t=f"{settings.BASE_DIR}/static/"
    param_t = os.path.getmtime(path_t)



    context['fileparam'] =param_t
    context['fileparam2'] =param_t



    return context
