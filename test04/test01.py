#file : test01.py
'''
msg = "숫자"
no = 10
print(msg + str(no))

msg1 = msg + msg
print(msg1)

length = len(msg1)
print('msg1의 길이 : ' + str(length))

msg = 'Hello World'

print('Hello' in msg)
print('Hello' not in msg)

for s in msg:
    print(s)
    no += 1

print(no)
print(len(msg))

# 연산자
no1 = 3
no2 = 5
print(no1 ** no2)
print(pow(no1, no2))

'''

'''
    자바의 삼항연산자
        (조건식) ? 조건식이 참일때 반환값 : 조건식이 거짓일때 반환값
        

# 삼항연산자
# 형식 ]      참일때 반환값 if 조건식   else   거짓일때 반환값

# 정수 하나를 입력받아서 짝수인지 홀수인지를 판별하세요.

# no = int(input('정수입렵 : '))
sno = input('정수 입력 :')
no = int(sno)
result = '홀수' if no % 2 == 1 else '짝수'
print('입력받은 정수 ', no, '는', result, '입니다.')
'''

# 멤버 연산자
no = 10
noList = [1, 2, 3, 4, 5]
result = '포함됩니다.' if no in noList else '포함되어 있지 않습니다.'
print('10은 noList에 ' + result)

print('# not int')
result = '포함되어 있지 않습니다.' if no not in noList else '포함됩니다.'
print('10은 noList에 ' + result)



