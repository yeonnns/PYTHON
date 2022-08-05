#file: test01.py


'''
print('1/0 = ', 1/0)
print('예외처리 예제 성공1')
'''

# 오류 발생하면 예외처리로 바로 이동
try:
    print('1/0 = ', 1/0)
    print('******1')
except ZeroDivisionError:
    print('정수를 0으로 나누지는 못합니다.')
    print('******2')

print('예외처리 예제 성공2')