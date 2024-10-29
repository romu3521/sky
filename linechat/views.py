from django.shortcuts import render

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging

import requests

logger = logging.getLogger(__name__)


@csrf_exempt
def line_webhook(request):
    
    CHANNEL_ACCESS_TOKEN = 'oYoxn4ytHWiGRWdVUXx8jPZG14cErc3At4O97tttDHEQDMUe5PdqBPkpbtjNHgSIHx0y0DDNs/VlPCRH23y1kROrNJNhik37k8yHHvj6A/URrhgu4KrjNnyHrhkC4yffsuc2aDFidf0SLAXsfyffewdB04t89/1O/w1cDnyilFU='  # 取得したチャネルアクセストークンに置き換え
    if True:
        body = json.loads(request.body)
        user_id="xxxxxx"

        if 'events' in body and len(body['events']) > 0:
            try:
                user_id = body['events'][0]['source']['userId']
                send_push_message(CHANNEL_ACCESS_TOKEN,user_id)
                return jsonresponse({'user_id': user_id}, status=200)
            except e:
                logger.error('エラーが発生しました: %s', request.body)


        else:
            logger.error('エラーが発生しました: %s', request.body)

            

    #GETです: b'{"destination":"U45e7e1d768298950e9599f5ab2277095","events":[{"type":"message","message":{"type":"text","id":"532461546153705994","quoteToken":"YFpDcAavfmWF9YFJWwjY27KHclGowKvSNT5rpN3Zplt7O1rD0vye5eqRY2jSBg4YpQOk99Ec6Qx8DHKVfaMlxj8ov9Hxf3yCzCmdEid7YFyL1t-vngRVW_GhXyfKmhdRCpyvYNgcX2kU7s-KL81itw","text":"\xe3\x81\x82\xe3\x81\x8b"},"webhookEventId":"01JBC28SZH5N1HC6RSNE7K8KYC","deliveryContext":{"isRedelivery":false},"timestamp":1730203117332,"source":{"type":"user","userId":"U6381a22590f3cac80158b0e045ea98d4"},"replyToken":"d79ea739a4664c6183456fa65dc1d739","mode":"active"}]}'

    
    logger.error('GETです: %s', request.body)


    return JsonResponse({'error': 'Invalid request'}, status=400)



def send_push_message(token,userid,message):
    url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    data = {
        'to': userid,
        'messages': [
            {
                'type': 'text',
                'text': f'user id をどうぞ「{message}」'
            }
        ]
    }
    
    # POSTリクエストを送信
    response = requests.post(url, headers=headers, json=data)
    
    # レスポンスの確認
    if response.status_code == 200:
        print('メッセージ送信成功:', response.json())
    else:
        print('メッセージ送信エラー:', response.status_code, response.text)
