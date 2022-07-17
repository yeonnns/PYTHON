# file: test03.py

import math as m

'''
    문제 1 ] 
        두 정수를 입략빋이서 사각형의 넓이를 계산해서 출력해주는 프로그램을 작성하세요
        

num = int(input('가로 입력:'))
num2 = int(input('세로 입력:'))


print('사각형의 넓이 : ', num*num2)
'''

'''
    문제 2 ] 
        반지금을 입력받아서 원의 넓이와 둘레를 계산해서 출력해주는 프로그램을 작성하세요


num3 = int(input('번지름 입력:'))
print('원의 넓이 : ', num3*num3*m.pi)
print('원의 둘레 : ', num3*2*m.pi)

'''
'''
msg = 'jennie'
print('1. msg : ', msg)
# msg[0] = 'J' ==> 문자열 데이터 자체는 변경 불가능하다.
msg = 'J' + msg[1:]
print('2. msg: ',msg)
# ==> 문자열 데이터 자체는 변경 불가능하다.
msg.upper()
print('3. msg: ',msg)
msg1 = msg.upper()
print('4. msg1: ',msg1)
'''

#문자열 슬라이싱
'''
msg = '나는 블랙핑크 제니가 좋아요!'
print(msg[0:3])
#msg 에서 '나는 '만 추출하고 싶다.
s1 = msg[:2]
print(s1)
# 변수 = 문자열[시작위치: 종료위치] ==> 시작위치에서부터 종료위치 이전까지 추출해서 문자열을 반환해준다. 리스트도 가능
#       이때 시작위치를 기술하지 않으면 자동적으로 처음위치를 의미하게 된다. 

s2 = msg[-4:]
print('msg[-4:]', s2)
# 인덱스를 음수로 입력하는 경우는 뒤부터 인덱스를 계산해서 해당 위치의 문자만 꺼내서 반환해준다.

s3 = msg[::-1]
print('msg[::-1] : ' , s3)
'''

'''
msg = 'python'
msg1 = msg*4
print('msg*4 : ', msg1)
print('+'*40)
print(msg)

length = len(msg) # msg의 길이를 반환
print('='*35)
print(length)
'''

