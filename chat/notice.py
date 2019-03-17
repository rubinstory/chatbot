#-*- coding: utf-8 -*-
import sys
sys.path.append('/usr/local/lib/python3.6/dist-packages')
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, date


before_two_weeks = str(date.today() - timedelta(100))
now = before_two_weeks[:4] + before_two_weeks[5:7] + before_two_weeks[8:]

year = 20181231
year = int(now)
n=1
active_dict = dict()
findname=[]
finddate = []

options = Options()
options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("disable-gpu")
broswer = webdriver.Chrome(executable_path='/Users/LeeJunYoung/Desktop/chatbot/chromedriver_mac',options=options)
url = 'https://ece.pusan.ac.kr/ece/40583/subview.do'
broswer.get(url)

broswer.find_element_by_id('srchWrd').send_keys('학과활동인정')
broswer.find_element_by_xpath('//*[@id="menu40583_obj255"]/div[2]/form[1]/div/div[2]/fieldset/span/input').submit()



while(True):
    try:
        date = broswer.find_element_by_xpath('//*[@id="menu40583_obj255"]/div[2]/form[2]/table/tbody/tr['+str(n)+']/td[4]').text
        date = int(date[0:4] + date[5:7] + date[8:10])
        if(date>=year):
            findname.append(broswer.find_element_by_xpath('//*[@id="menu40583_obj255"]/div[2]/form[2]/table/tbody/tr['+str(n)+']/td[2]/a/strong').text)
            finddate.append(broswer.find_element_by_xpath('//*[@id="menu40583_obj255"]/div[2]/form[2]/table/tbody/tr['+str(n)+']/td[4]').text)    
        n=n+1
    except Exception:
        break
active_dict = dict(zip(findname,finddate))
name_list = list(active_dict.keys())
time_list = list(active_dict.values())
print(name_list)
print(time_list)
broswer.quit()
