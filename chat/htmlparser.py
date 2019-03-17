from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# selenium 다운받아야함
from bs4 import BeautifulSoup
import time
import json

percent = []
name = []
lib_dict = dict()
options = webdriver.ChromeOptions()
options.add_argument('headless')
brower = webdriver.Chrome(executable_path='/Users/LeeJunYoung/Desktop/chatbot/chromedriver_mac',options=options)
# Chrome driver사용  webdrvier.Chrome('Chromedriver의 절대경로') 맥 윈도우 리눅스 각각 다르므로 다운받아야함 맥 리눅스의 경우 .exe를 빼면 됨
url = 'https://lib.pusan.ac.kr/'
brower.get(url)
brower.find_element_by_xpath("//*[@id='quick-menu']/div/ul/li[6]/a").click()
# 원격으로 부산대학교 도서관 열람실 좌석 버튼 클릭(자바스크립트를 렌더링하는 방식이라 클릭하지 않으면 열람식 이용율을 크롤링 할 수 없음
time.sleep(3)
#brower.implicitly_wait()는 살짝 오류가 나길래 그냥 time.sleep을 사용

for i in range(1,16):
    #리스트로 열람실 위치, 이용율 정리
    name.append(brower.find_element_by_xpath('//*[@id="library-seats-table"]/tbody/tr['+str(i)+']/td[2]/a').text)
    percent.append(brower.find_element_by_xpath('//*[@id="library-seats-table"]/tbody/tr['+str(i)+']/td[6]/span/span[2]').text)
    lib_dict=dict(zip(name,percent))
    # json형식으로 만들기 위해 리스트를 딕셔너리 형태로 만들어 놓음

brower.quit()
#brower종료

saebyeok_position = list(lib_dict.keys())[1:6]
saebyeok_position.append(list(lib_dict.keys())[7])
for i in range(len(saebyeok_position)):
	saebyeok_position[i] = saebyeok_position[i][6:]

saebyeok_percent = list(lib_dict.values())[1:6]
saebyeok_percent.append(list(lib_dict.values())[7])

keonseol_position = list(lib_dict.keys())[9:11]
for i in range(len(keonseol_position)):
	keonseol_position[i] = keonseol_position[i][6:]

keonseol_percent = list(lib_dict.values())[9:11]
