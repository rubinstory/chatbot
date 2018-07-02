from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
 
 
 
def keyboard(request):
 
    return JsonResponse({
        'type':'buttons',
        'buttons':['Today','Tommorrow']
    })
 
@csrf_exempt
def answer(request):
 
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']
 
    if datacontent == 'Today':
        today = "Today's meal"
 
        return JsonResponse({
                'message': {
                    'text': today
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['Today','Tommorrow']
                }
 
            })
 
    elif datacontent == 'Tommorrow':
        tomorrow = "Tommorow's meal"
 
        return JsonResponse({
                'message': {
                    'text': tomorrow
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['Today','Tommorrow']
                }
 
            })
 
