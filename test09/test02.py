#file: test02.py

'''
#nameError 오류 클래스에 해당하는 객체
try:
    abc()
except NameError as msg:
    print('Error - ', msg)
'''
'''
# try~except~else : else 사용시 except 필수
def division():
    for n in range(0,5): # n 0~4까지 대입
        try:
            print(10 / n)
        except ZeroDivisionError:
            print('0으로 정수를 나누려고 합니다')
        except :
            print('오류발생')
        else:
            print('Success')

division()
'''

print(1)
print(2)
print(3)
raise Exception('오류 발생시키기')
print(4)
print(5)
print(6)
print(7)
