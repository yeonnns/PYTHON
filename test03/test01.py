#file: test01.py

'''
no = '10'
print('type of no : ', type(no))

no = int(no) # ==> 정수 형태의 문자열을 정수로 변환해준다. 자바의 integer.parseint()와 같은 기능
print('type of no : ', type(no))

num = int(input('정수 입력 : ')) # 자바의 Scanner 클래스의 nextLine()과 같은 기능
print(num)
print('type of num :', type(num))

msg = '입력받은 숫자는 ' + str(num) + ' 입니다.' # type이 다른 함수는 결합 할 수 없음
print(msg)
'''

'''
no1 = 10
no2 = 3

print("no1 + no2 = ", no1 + no2)
print("no1 - no2 = ", no1 - no2)
print("no1 * no2 = ", no1 * no2)
print("no1 / no2 = ", no1 / no2) # 나눈 결과를 실수 형태로 표현
print("no1 % no2 = ", no1 % no2)
print("no1 // no2 = ", no1 // no2) # 나눈 결과의 몫만 반환
print("no1 ** no2 = ", no1 ** no2) # 앞의 숫자를 뒤의 숫자로 거듭제곱, no1의 no2승
'''

'''
import sys

print("표현 가능한 최대 숫자 : ", sys.maxsize)
'''

'''
no1 = 10 + 5j
no2 = 100 + 100j
print(no1)
print(no2)

print(no1 + no2) #  실수부 허수부는 각각 계산됨
'''

'''
# 수치자료형 함수들
print(abs(-100))
print(round(3.14))
print(round(10.5))
print(int(3.14))
print(int(-3.14))
print(float(3))
print(complex(3.14, 3))
print(complex(100))
'''
'''
result = divmod(17, 2)
print(result) # 앞의 숫자를 두번째 숫자로 나눈 몫을 앞에, 나머지를 뒤에 표현한다.
print('type of result : ', type(result))
# type of result :  <class 'tuple'> 리스트 형태의 튜플, 자바의 배열처럼 다루면 됨, 수정은 불가

mok = result[0]
rest = result[1]

print('몫 : ', mok, ', 나머지 : ', rest)
'''
'''
result = pow(10, 3)
print(result) # 10 ** 3 과같은 결과


import math

PI = math.pi
E = math.e

print("math.pi : ", PI)
print('math.e : ', E)
print('math.floor(PI) :', math.floor(PI))
print('math.trunc(PI) :', math.trunc(PI))
'''

def abc():
    return '나는 abc'

import math
print(math.sqrt(16))
print(math.sqrt(2))
