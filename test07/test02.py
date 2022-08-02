#file: test02.py
'''
# 매개변수 두개 지정
def line(count=80, char='-'):
    for i in range(0,count):
        print(char, sep='',end='|')
    print()

print('재미있는 Python!')
line(30)


line(5,'black')

line(char='pink', count=10)
line() #매개변수의 초기값 사용해서 함수를 호출
'''

# n~m 사이에 값 반환
def sum1(n=1, m=100):
    if n > m:
        n, m = m, n

    hap = 0
    for i in range(n, m+1):
        hap += i
    return hap

hap = sum1(1,3) + sum1(1,5) + sum1(1,10)
print('hap: ', hap)


'''
    n부터 m 까지의 곲을 반환해주는 함수(facto)를 제작하고
    매개변수의 초기값은 n은 1 m은 10으로 한다.
    5~21 까지의 곱을 구해서 출력하세요
    
'''

def facto(n=1, m=10):
    if n > m:
        n,m = m,n
    gop = 1
    for n in range(n, m+1):
        gop *= n
    return gop

print('5~21 까지의 곱 : ', facto(5,21))


# 반환값이 여러개인 함수
def calc(a,b):
    if a > b:
        a,b = b,a
    return a + b, b - a, a * b, b / a, b % a

print('calc(3,10) : ', calc(3,10))

t1 = calc(3,10)
print('type of t1 : ', type(t1))

l1 = list(t1)
l1[0] = 14

t1 = tuple(l1)

print(t1)

'''
def print(a):
    return 'print: [ ' + a + ' ]'
    
print('abc')
==> 기존의 함수의 기능을 바꿨기 때문에 원래 기능을 사용할 수 없게 된다.
'''