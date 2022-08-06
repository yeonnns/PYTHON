#file: test02.py

'''
스크래핑 : 데이터가 포함된 웹 문서 전체를 가져오는 작업(태그가 포함되어 있다.)
크롤링  : 웹문서에서 워나는 데이터들만 추출하는 작업
마이닝  : 수집한 데이터를 사용가능한 데이터로 변환시켜서 저장하는 작업

'''

'''
    모듈 설치하는 방법
    
        명령 ] 
            pip install 모듈이름 : 리룩스 yum 처럼 모듈 설치
            pip install requests
            
    url = http://www.naver.com/robots.txt
    
    X
    http://www.naver.com/abc/1,html
    http://web.naver.com
    
'''

import requests


url = 'http://www.naver.com/robots.txt'

resp = requests.get(url)

#응답 코드 확인
print('응답코드 : ', resp.status_code)
#응답 내용 확인
print('응답내용 : ', resp.text, sep='', end='\n-----------------')

#네이버 대문페이지 읽어오세요(스크래핑)
resp = req.get('http://www.naver.com')
resp_code = resp.status_code
if resp_code == 200:
    print(resp.text)
    print('응답코드 데이터 타입', type(resp.text))