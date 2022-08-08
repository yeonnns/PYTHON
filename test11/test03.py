#file: test03.py
'''
    교보문구 메인사이트에서
    스토리 k 섹션의 리스트를 가져와서 출력하세요.

'''

#import requests as req
import selenium
from selenium import webdriver
url = 'http://www.kyobobook.co.kr/index.laf'
path = 'c://app/chromedriver/chromedriver.exe'


#resp = req.get(url)
#print(resp.text)

driver = webdriver.Chrome(path)
driver.get(url)

els = driver.find_element_by_class_name('.title')
print('*************', len(els))
for e in els:
    print(e.text)
