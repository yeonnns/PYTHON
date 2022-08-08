# file: test02.py

import selenium
from selenium import webdriver

url = 'http://192.168.56.1/www/'
path = 'c://app/chromedriver/chromedriver.exe'

driver = webdriver.Chrome(path)
driver.get(url)

'''
    Selenium HTML로 접근하기
    
        단일 객체
            find_element_by_id()            ==> 아이디를 이용해서 선택하는 방법
            fing_element_by_selector()      ==> css 선택자를 이용해서 선택하는 방법 ==> 처음 발견된 태그 하나
            find_element_by_class_name()   ==> 클래스이름을 이용해서 선택하는 방법 ==> 처음 발견된 태그 하나
            ....
        복수 객체
            find_elements_by_css_selector() ==> css 선택자를 이용해서 선택하는 방법  ==> 선택자에 해당하는 모든 태그를 선택
            find_elements_by_class_name()   ==> 클래스 이름에 해당하는 모든 태그를 선택하는 방법
            find_elements_by_tag_name()     ==> 태그 이름으로 선택하는 방법
       
'''

els = driver.find_elements_by_css_selector('#mList div')
print('*************', len(els))
for e in els:
    print(e.text)
    print(e.get_attribute('id'), ' - ', e.text)

'''
    selenium은 브라우저를 직접 제어하기 떄문에 사람이 직접 컨트롤 하듯이
    마우스 클릭, 키보드 입력 , 자바스크립트이벤트 처리를 할 수 있다.
    
        마우스 클릭          : click()
        키보드 입력          : send_keys()
        자바스크립트 삽입     : execute_script()  
        입력양식을 전송       : submit()
        스크린샷을           : screenshot(파일이름)
        글자 지워주는 함수    : clear()
        뒤로가기             : back()
        앞으로 가기          : forward()
        
'''
