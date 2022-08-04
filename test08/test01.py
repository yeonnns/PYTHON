#file: test01.py

'''
# g, h : 전역변수
g = 10
h = 5

def f(a):
    h = a+10
    b = h + a + g

    return b

print(f(h))
print('h :', h)
'''
'''
# global 키워드 활용
h = 5
print('f() 함수 호출 전 h :', h)
def f(a):
    global h
    h = a + 10

    return h

print('f(10) : ', f(10))
print('h : ',h)
'''

'''
# 오류
g = 10
def f():
    a = g # g : 전역변수
    g = 20 # g : 지역변수

    return a

print(f())
'''
'''
g = 10
print('함수 호출 전 g :', g)
def f():
    global g
    a = g
    g = 20

    return a

print('f() : ', f())
print('g : ', g)
'''

no = 10 # 전역변수

def f1():
    no = 20 # 지역변수
    def g1():
        print(no)
    g1()

print('f() : ', end='')
f1()
print('no : ', no)