from __future__ import unicode_literals
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json
import random as rand

ftp_password = 'wnff.6308.2'
doorlock_password = '1234'

def index(request):
    return HttpResponse("This is Beta Bot.")

def keyboard(request):
    
    return JsonResponse({
                        'type':'buttons',
                        'buttons':['청소조 확인', 'FTP서버 비밀번호 확인', '동방 비밀번호 확인']
                        })

@csrf_exempt
def message(request):
    
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']
    
    response = 'nothing'
    
    if datacontent == '청소조 확인':
        response = '이름을 입력하세요.'

        return JsonResponse({
                        'message': {
                        'text': response
                        },
                        'keyboard': {
                        'type':'text'
                        }
                        })

    elif datacontent == 'FTP서버 비밀번호 확인':
        response = ftp_password
    
    elif datacontent == '동방 비밀번호 확인':
        response = doorlock_password
    
    else: #이름이 입력된 경우
        entered_name = datacontent
    
    
    
    return JsonResponse({
                        'message': {
                        'text': response
                        },
                        'keyboard': {
                        'type':'buttons',
                        'buttons':['청소조 확인', 'FTP서버 비밀번호 확인', '동방 비밀번호 확인']
                        }
                        })


