#file: test02.py
'''
import test01 as t1

t1.f1()
'''
'''
import string
print(dir(string))
'''
'''
import math # 모듈 이름으로 임포트 
'''
from math import pi # math 모듈내의 pi 상수를 임포트해서 사용하겠습니다.
# 반지름을 입력받아서 원의 넓이를 출력해주는 프로그램을 작성하세요.

def printArea():
    rad = int(input('반지름 : '))
#    area = rad ** 2 * math.pi
    area = rad ** 2 * pi
    print('입력받은 반지름 %3d 를 가지는 원의 넓이는 %7.2f 입니다.' %(rad, area))
printArea()