#-*- coding: utf-8 -*-
from selenium import webdriver
# selenium 다운받아야함
from bs4 import BeautifulSoup
import time

percent = []
name = []
lib_dict = dict()
brower = webdriver.PhantomJS('/Users/LeeJunYoung/kakao/phantomjs/bin/phantomjs')
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

print(lib_dict)

brower.quit()
#brower종료

