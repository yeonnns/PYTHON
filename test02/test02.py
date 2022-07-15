# file: test02.py
import keyword

print('파이썬 예약어 리스트 : ')
print(keyword.kwlist)
print()
print('파이썬 예약어 갯수 : ')
print(len(keyword.kwlist))


def abc():
    pass


print(sum([1, 2, 3, 4, 5]))
print()
print(abs(3))
print(abs(-3))

print()
print('- max() - ')
print(max(10, 2, 3))
print(max([1, 12, 5, 6, 3, 9]))
print(max('Hello World!'))

print(min((1, 4, 3, -2)))

"""
    ==> 여러행 주석

    파이썬의 경우 자료형 중
    변경 가능한 자료형과 
    변경 불가능한 자료형을 구분해주는 것이 중요하다.
"""

# pow() ==> 한줄 주석
print()
print('- pow() -')
print('2의 3승 : ', pow(2, 3))  # 여러 데이터를 동시에 출력할 경우는 , 를 구분자로 나열하면 된다.
print('3의 -2승 : ', pow(3, -2))  # ==> 1 / 9

# chr() ==> 아스키 코드값을 입력하면 문자를 반환해주는 함수
print()
print('아스키 코드 97 에 해당하는 문자 : ', chr(97))

# ord(문자)
print()
print('대분자 J 의 아스키 코드값 : ', ord('J'))

'''
    파이썬의 경우 문자열표현할 때 
    큰따옴표와(") 작은 따옴표(')를 동시에 사용할 수 있다.
    대신 큰따옴표로 시작했으면 큰따옴표로 마쳐야한다.
'''

# str() ==> 데이터를 문자열로 변환해서 반환해주는 함수
print()
print('10 : ', 10)
print('str(10) : ', str(10))
print('str["jennie", "jisoo"]) : ', str(["jennie", "jisoo"]))

# var attr = "class=\"w3-col\""; ==> var str = 'class="w3-col"';


# range([start, ]stop[, step])
print()
rn = range(1, 11)
print('1 ~ 10 까지 : ', rn)

for no in range(1, 11):
    print(no)

print()

for no in range(3, 11, 2):
    print(no)

# 참고 ] 파이썬 2.xx 버젼까지는 출력함수의 형식이
#       print 데이터
#       print() 의 형태로 사용하기 시작은 3.0 부터 시작....

a1 = 10
a2 = '10'

print()
print('a1 : ', a1)
print('a2 : ', a2)
print()
print('type of a1 : ', type(a1))
print('type of a2 : ', type(a2))
print('type of rn : ', type(rn))
print()

import test03

print('test03.mno : ', test03.mno)

# test03 = '여기는 test03 변수'

# print('test03.mno : ', test03.mno)
tel = None

print('type of tel : ', type(tel))

print(tel)

del tel

print(tel)

'''
if(a == b && .....){
    조건식이 길어지는 경우 자바는 줄바꿈해도 상관없다.
}
파이썬의 경우 한줄로 표현되어야될 문장은
\  를 이용해서 줄바꿈해서 처리해야 한다.
'''

no1 = 2
no2 = 3

if (no1 > 0) & (no2 < 10) & \
        (no1 % 2 == 0) & \
        (no2 % 2 == 1):  # \ ==> 다음행의 내용은 이행에 이어지는 내용입니다.
    print()