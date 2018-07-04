from __future__ import unicode_literals
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json
import random as rand


def index(request):
    return HttpResponse("This is Beta Bot.")

def keyboard(request):
    
    return JsonResponse({
                            'type':'buttons',
                            'buttons':['가위','바위','보']
                        })

@csrf_exempt
def message(request):
    
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']
    
    num = int(rand.random() * 10) % 3

    if num == 0:
        choose = '가위'
    elif num == 1 :
        choose = '바위'
    elif num == 2:
        choose = '보'

    result = "당신의 수 : {}\n 컴퓨터의 수 : {}\n".format(datacontent,choose)

    if datacontent == '가위':
        if choose == '가위':
            result += '비겼습니다.'

        elif choose == '바위':
            result += '졌습니다.'

        elif choose == '보':
            result += '이겼습니다.'


    elif datacontent == '바위':
        if choose == '바위':
            result += '비겼습니다.'

        elif choose == '보':
            result += '졌습니다.'

        elif choose == '가위':
            result += '이겼습니다.'

    elif datacontent == '보':
        if choose == '보':
            result += '비겼습니다.'

        elif choose == '가위':
            result += '졌습니다.'

        elif choose == '바위':
            result += '이겼습니다.'

    return JsonResponse({
                            'message': {
                                'text': result
                            },
                            'keyboard': {
                                'type':'buttons',
                                'buttons':['가위','바위','보']
                            }

                        })


