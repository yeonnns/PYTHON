#file: test03.py


import requests as req
from bs4 import BeautifulSoup

'''
    BeautifulSoup
        ==> 홈페이지 내 데이터를 쉽게 추출할 수 있도록 도와주는 
        파이썬 외부 라이브러리
        
        웹 문수 내 수많은 html 태그들을 파서(parser)를 활용해 
        사용하기 편한 파이썬 객체로 만들어서 제공해준다.
        --> html 문서 외에 xml 파서도 제공
        
        웻문서의 구조를 숙제하고 있다면
        아주 편하게 원하는 데이터틑 추출해서 활용 할수 있다.
       
       
        pip install beautifulsoup4

'''

url = 'http://www.naver.com'
resp = req.get(url)

htmlcode = ''
if resp.status_code == 200:
    htmlcode = resp.text

#BeautifulSoup 이용해서 파싱하는 방법
soup = BeautifulSoup(htmlcode, 'html.parser')

#들여쓰기 정렬
#print(soup.prettify())

'''
#a 태그 thumb 클래스
result = soup.find.all('a', 'thumb')
news_list = []
for r in result:
    #img 의 alt 속성값
    news_list.append(r.find('img')['alt'])

# 결과 출력
print(news_list)
'''

result = soup.find.all('a', '_NM_THEME_CATE')
cate_list = []
for c in result:
    cate_list.append(c.find('a').string)

print(cate_list)


