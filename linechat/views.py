from django.shortcuts import render

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def line_webhook(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        
        if 'events' in body and len(body['events']) > 0:
            user_id = body['events'][0]['source']['userId']
            
            return JsonResponse({'user_id': user_id}, status=200)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
