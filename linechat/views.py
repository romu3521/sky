from django.shortcuts import render

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
logger = logging.getLogger(__name__)

@csrf_exempt
def line_webhook(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        user_id="xxxxxx"

        if 'events' in body and len(body['events']) > 0:
            print("aa")

            #user_id = body['events'][0]['source']['userId']
        else:
            logger.error('エラーが発生しました: %s', request.body)

            

            return JsonResponse({'user_id': user_id}, status=200)
    
    logger.error('エラーが発生しました: %s', "get Access")
    return JsonResponse({'error': 'Invalid request'}, status=400)



