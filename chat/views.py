from __future__ import unicode_literals
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json
import sys
sys.path.append('/usr/local/lib/python3.6/dist-packages')
import openpyxl
from datetime import date

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

        # 엑셀파일 열기
        list_file = openpyxl.load_workbook('/home/rubinstory1/chatbot/chat/list.xlsx')

        # 현재 Active Sheet 얻기
        ws = list_file.active
 
        for row in ws.rows:
            index = 0
            team_num = row[index].value
            index += 1
            while index < len(row):
                list_name = row[index].value
                if list_name == datacontent:
                    response = "\"{}\"님의 청소조는 {}조 입니다.".format(datacontent,team_num)

                    today = str(date.today())
                    weekend = ['토요일', '일요일']
                    schedule_file = openpyxl.load_workbook('/home/rubinstory1/chatbot/chat/schedule.xlsx')
                    wt = schedule_file.active
                    for irow in wt.rows:
                        time = str(irow[0].value)[0:10]
                        day = irow[1].value
                        if day not in weekend and time >= today:
                            cleaner = (irow[2].value)[0]
                            if str(team_num) == cleaner:
                                response += "\n다음 청소 날짜는 {}, {}입니다.".format(time, day)
                                if (time == today):
                                    response += "\n오늘이네요! 꼭 청소하러 와주세요!"
                                schedule_file.close()
                                list_file.close()
                                return JsonResponse({
                                    'message': {
                                    'text': response
                                    },
                                    'keyboard': {
                                    'type':'buttons',
                                    'buttons':['청소조 확인', 'FTP서버 비밀번호 확인', '동방 비밀번호 확인']
                                    }
                                })
                                
                    
                    schedule_file.close()
                    list_file.close()
                    return JsonResponse({
                        'message': {
                        'text': response
                        },
                        'keyboard': {
                        'type':'buttons',
                        'buttons':['청소조 확인', 'FTP서버 비밀번호 확인', '동방 비밀번호 확인']
                        }
                        })
                else:
                    response = "{}님은 청소조 명단에 없습니다.\n회장단에게 문의해주세요.".format(datacontent,team_num)
                    index += 1

        list_file.close()
    
    
    
    return JsonResponse({
                        'message': {
                        'text': response
                        },
                        'keyboard': {
                        'type':'buttons',
                        'buttons':['청소조 확인', 'FTP서버 비밀번호 확인', '동방 비밀번호 확인']
                        }
                        })


