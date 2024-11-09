from django.http import HttpResponse,JsonResponse
import json
import html
from basecom.serializers import FoCommentsSerializer
from basecom.models import FoComments,FoPosts
from rest_framework.exceptions import NotFound

def drfcmt(request):
    params = dict()

    if request.method=="POST" or True:
        
        data = json.loads(request.body.decode('utf-8'))
        try:
            pt=FoPosts.objects.get(id=data["article"],is_public_cmt=True)
        except Exception as e:
            print(e)
            raise NotFound("指定されたリソースは存在しません。")

        p=FoComments.objects.filter(parent_post__id=data["article"],parent_post__is_public_cmt=True).order_by('-created_at')[:5]

        serializer=(FoCommentsSerializer(p,many=True))

        if (not data["comment"]=="") and (not data["name"]==""):
            try:
                pt=FoPosts.objects.get(id=data["article"])
                i = FoComments(display_authorname=html.escape(data["name"]),contact_mail=html.escape(data["mail"]),parent_post=pt,comment_content=html.escape(data["comment"]))
                i.save()
            except Exception as e:
                print(e)

        params=serializer.data
        params.reverse()
        
    return JsonResponse(params, safe=False)
