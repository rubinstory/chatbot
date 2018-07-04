from __future__ import unicode_literals
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json


def index(request):
    return HttpResponse("This is Beta Bot.")

def keyboard(request):
    
    return JsonResponse({
                            'type':'buttons',
                            'buttons':['오늘','내일']
                        })

@csrf_exempt
def message(request):
    
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']
    
    if datacontent == '오늘':
        today = "오늘의 급식"
        
        return JsonResponse({
                                'message': {
                                    'text': today
                                },
                                'keyboard': {
                                    'type':'buttons',
                                    'buttons':['오늘','내일']
                                }

                            })
    
    elif datacontent == '내일':
        tomorrow = "내일의 급식"
        
        return JsonResponse({
                                'message': {
                                    'text': tomorrow
                                },
                                'keyboard': {
                                    'type':'buttons',
                                    'buttons':['오늘','내일']
                                }
                            
                            })


