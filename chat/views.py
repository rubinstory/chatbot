from __future__ import unicode_literals
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json
import sys
#sys.path.append('/usr/local/lib/python3.6/dist-packages')
import openpyxl
from datetime import date

sys.path.append('/Users/LeeJunYoung/Desktop/chatbot/chat')
from htmlparser import saebyeok_position, saebyeok_percent, keonseol_percent, keonseol_position
from notice import name_list, time_list

temp = open('/Users/LeeJunYoung/Desktop/chatbot/chat/ftp_password.txt', 'r')
ftp_password = temp.readline()

temp = open('/Users/LeeJunYoung/Desktop/chatbot/chat/doorlock_password.txt', 'r')
doorlock_password = temp.readline()

def index(request):
    return HttpResponse("This is Beta Bot.")

def keyboard(request):
    
    return JsonResponse({
                        'type':'buttons',
                        'buttons':['학과활동 확인', '도서관 좌석 상태 확인', '청소조 확인', 'FTP서버 비밀번호 확인', '동방 비밀번호 확인']
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

    elif datacontent == '학과활동 확인':
        if (len(name_list) < 1):
            response = '2주 내에 작성된 학과활동 게시물이 없습니다.'
            return JsonResponse({
                                'message': {
                                    'text': response
                                },
                                'keyboard': {
                                    'type':'buttons',
                                    'buttons':['학과활동 확인', '도서관 좌석 상태 확인', '청소조 확인', 'FTP서버 비밀번호 확인', '동방 비밀번호 확인']
                                    }
                                })
        else:
            response = ''
            for i in range(len(name_list)):
                response += name_list[i]
                response += ": "
                response += time_list[i]
                response += "\n\n"
            return JsonResponse({
                                'message': {
                                    'text': response
                                },
                                'keyboard': {
                                    'type':'buttons',
                                    'buttons':['학과활동 확인', '도서관 좌석 상태 확인', '청소조 확인', 'FTP서버 비밀번호 확인', '동방 비밀번호 확인']
                                    }
                                })


    elif datacontent == '도서관 좌석 상태 확인':
        total_percent = 0
        for i in range(len(saebyeok_percent)):
            total_percent += float((saebyeok_percent[i])[:-1])
        for i in range(len(keonseol_percent)):
            total_percent += float((keonseol_percent[i])[i:-1])

        total_percent /= ( len(saebyeok_percent) + len(keonseol_percent) )
        response = "현재 도서관들의 평균 좌석 점유율은 {}%입니다.\n".format("%0.2f" % total_percent)

        if (total_percent >= 65.0):
            response += "시험기간인가 보네요!\n"

        response += '도서관을 선택하세요.\n(자유석으로 운영하는 곳은 조회가 불가능합니다)'
        return JsonResponse({
                                'message': {
                                'text': response
                                },
                                'keyboard': {
                                'type':'buttons',
                                'buttons':['새벽벌', '건설관']
                                }
                                })

    elif datacontent == '새벽벌' or datacontent == '건설관':
        if datacontent == '새벽벌':
            response = ''
            for i in range(len(saebyeok_position)):
                response += saebyeok_position[i]
                response += ' '
                response += saebyeok_percent[i]
                response += '\n'
        else:
            response = ''
            for i in range(len(keonseol_position)):
                response += keonseol_position[i]
                response += ' '
                response += keonseol_percent[i]
                response += '\n'

        return JsonResponse({
                                'message': {
                                    'text': response
                                },
                                'keyboard': {
                                    'type':'buttons',
                                    'buttons':['학과활동 확인', '도서관 좌석 상태 확인', '청소조 확인', 'FTP서버 비밀번호 확인', '동방 비밀번호 확인']
                                    }
                                })
    
    
    
    elif datacontent == 'FTP서버 비밀번호 확인':
        response = ftp_password
    
    elif datacontent == '동방 비밀번호 확인':
        response = doorlock_password
        response += '지금은 베타테스트 중입니다. 이건 진짜 비밀번호가 아닙니다.'
    
    else: #이름이 입력된 경우

        # 엑셀파일 열기
        list_file = openpyxl.load_workbook('/Users/LeeJunYoung/Desktop/chatbot/chat/list.xlsx')

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
                    schedule_file = openpyxl.load_workbook('/Users/LeeJunYoung/Desktop/chatbot/chat/schedule.xlsx')
                    wt = schedule_file.active
                    for irow in wt.rows:
                        time = str(irow[0].value)[0:10]
                        day = irow[1].value
                        if day not in weekend and time >= today:
                            cleaner = (irow[2].value)[0]
                            if str(team_num) == cleaner:
                                response += "\n다음 청소 날짜는 \n{}, {}입니다.".format(time, day)
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
                                    'buttons':['학과활동 확인', '도서관 좌석 상태 확인', '청소조 확인', 'FTP서버 비밀번호 확인', '동방 비밀번호 확인']
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
                        'buttons':['학과활동 확인', '도서관 좌석 상태 확인', '청소조 확인', 'FTP서버 비밀번호 확인', '동방 비밀번호 확인']
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
                        'buttons':['학과활동 확인', '도서관 좌석 상태 확인', '청소조 확인', 'FTP서버 비밀번호 확인', '동방 비밀번호 확인']
                        }
                        })


