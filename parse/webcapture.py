from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# 웹페이저를 전체화면으로 나타내기 위해 부름

def capture(url,seat):
    options = Options()
    options.add_argument('--start-fullscreen')
    # 전체화면
    driver = webdriver.Chrome(executable_path='C:\\Users\\USER\\Desktop\\chromedriver_win32\\chromedriver.exe', chrome_options=options)
    # htmlparser와 같이 절대경로 맥 윈도우 리눅스 각각 따로 chromedriver를 받아야함 
    driver.get(url)
    # 해당 주소로 들어가는 역할
    driver.implicitly_wait(1)
    # 실행후 1초동안 기다린다
    driver.save_screenshot(seat)
    # 스크린샷을 저장한다.
    driver.quit()
    # 웹 종료
    
# 이 밑은 그냥 어느 열람실을 캡쳐할지 나타내는 코드 
select1 = eval(input('1: 새벽벌, 2: 건설관, 3: 나노생명과학도서관\n'))

if select1 == 1:
    select2 = eval(input('1: 2층, 2: 3층, 3: 4층\n'))
    
    if select2 == 1:
        select3 = eval(input('1: 1열람실, 2: 1노트북 열람실\n'))
        
        if select3 == 1:
            url = 'http://seat.pusan.ac.kr/Clicker/UserSeat/20170307140519269'
            seat = '새별벌 2층 1열람실.png'
            capture(url,seat)
            
        elif select3 == 2:
            url = 'http://seat.pusan.ac.kr/Clicker/UserSeat/20170307140541333'
            seat = '새별벌 2층 1노트북 열람실.png'
            capture(url,seat)
            
        else:
            print('입력오류')

            
    elif select2 == 2:
        select3 = eval(input('1: 2-1열람실, 2: 2-2열람실\n'))
        
        if select3 == 1:
            url = 'http://seat.pusan.ac.kr/Clicker/UserSeat/20170307140600159'
            seat = '새별벌 3층 2-1열람실.png'
            capture(url,seat)
            
        elif select3 == 2:
            url = 'http://seat.pusan.ac.kr/Clicker/UserSeat/20170307140626602'
            seat = '새별벌 3층 2-2열람실.png'
            capture(url,seat)
            
        else:
            print('입력오류')

            
    elif select2 == 3:
        select3 = eval(input('1: 3-1열람실, 2: 3-2열람실, 3: 대학원 열람실, 4: 2노트북 열람실\n'))
        
        if select3 == 1:
            url = 'http://seat.pusan.ac.kr/Clicker/UserSeat/20170307140642163'
            seat = '새별벌 4층 3-1열람실.png'
            capture(url,seat)
            
        elif select3 == 2:
            url = 'http://seat.pusan.ac.kr/Clicker/UserSeat/20170307140701749'
            seat = '새별벌 4층 3-2열람실.png'
            capture(url,seat)
            
        elif select3 == 3:
            url = 'http://seat.pusan.ac.kr/Clicker/UserSeat/20170307142631880'
            seat = '새별벌 4층 대학원 열람실.png'
            capture(url,seat)
            
        elif select3 == 4:
            url = 'http://seat.pusan.ac.kr/Clicker/UserSeat/20170307140740868'
            seat = '새별벌 4층 2노트북 열람실.png'
            capture(url,seat)
            
        else:
            print('입력오류')

    else:
        print('입력 오류')

elif select1 == 2:
    
    select2 = eval(input('1: 3층, 2: 4층\n'))

    if select2 == 1:
        select3 = eval(input('1: 제1열람실, 2: 제2열람실\n'))
        
        if select3 == 1:
            url = 'http://seat.pusan.ac.kr/Clicker/UserSeat/20170307141524499'
            seat = '건설관 3층 제1열람실.png'
            capture(url,seat)
            
        elif select3 == 2:
            url = 'http://seat.pusan.ac.kr/Clicker/UserSeat/20170307141609419'
            seat = '건설관 3층 제2열람실.png'
            capture(url,seat)
            
        else:
            print('입력오류')
            
    elif select2 == 2:
        select3 = eval(input('1: 제3 열람실, 2: 대학원/강사 열람실\n'))
        
        if select3 == 1:
            url = 'http://seat.pusan.ac.kr/Clicker/UserSeat/20170307141630635'
            seat = '건설관 4층 제3열람실.png'
            capture(url,seat)
            
        elif select3 == 2:
            url = 'http://seat.pusan.ac.kr/Clicker/UserSeat/20170307141714809'
            seat = '건설관 4층 대학원/강사 열람실.png'
            capture(url,seat)
            
        else:
            print('입력오류')
        
    else:
        print('입력오류')
        
elif select1 == 3:
    select2 = eval(input('1: 제 1열람실, 2: 제 2열람실, 3: 제 3열람실\n'))
    
    if select2 == 1:
        url = 'http://seat.pusan.ac.kr/Clicker/UserSeat/20170418134020338'
        seat = '나노생명과학도서관 제1 열람실.png'
        capture(url,seat)
        
    elif select2 == 2:
        url = 'http://seat.pusan.ac.kr/Clicker/UserSeat/20170418140747110'
        seat = '나노생명과학도서관 제2 열람실.png'
        capture(url,seat)
        
    elif select2 == 3:
        url = 'http://seat.pusan.ac.kr/Clicker/UserSeat/20170418141008465'
        seat = '나노생명과학도서관 제3 열람실.png'
        capture(url,seat)
        
    else:
        print('입력오류')
        
else:
    print('입력 오류')
