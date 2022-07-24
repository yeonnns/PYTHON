# file: test.3.py

'''
    정수를 입력받아서
    입력받은 정수가 홀수인지, 짝수인지 판별하세요

no = int(input('정수입력 : '))
result = '홀수입니다.'
if no % 2 == 0 :
    result = '짝수입니다.'
print('입력받은 정수', no, '는 ', result)


# 형식화 문자열
msg = '이름 : {0}, 나이 : {2}, 메일 : {1}'.format('jennie', 'jennie@githrd.comm', 27)

print(type(msg))
print(msg)
'''

# if else
no = int(input('정수입력 : '))
'''
if no % 2 == 0:
    result = '짝수입니다.'
else:
    result = '홀수입니다.'
print('입력받은 정수{0} 는 {1}'.format(no, result))

if no == 0:
    result = '0입니다.'
elif no % 2 ==0:
    result = '짝수입니다.'
else:
    result = '홀수입니다.'

print('입력받은 정수 {0} 은 {1}'.format(no, result))

윤/평년

윤년 : 4로 나누어떨어짐, 100으로 나누어 떨어지지 않고, 400으로 나누어 떨어짐

'''

if no % 4 == 0 & no % 400 == 0 & no % 100 != 0:
   result = "윤년입니다."
else :
    result = "평년입니다."


print('입력받은 정수 {0} 은 {1}'.format(no, result))














