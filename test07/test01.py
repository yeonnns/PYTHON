#file: test.py

def add(a,b):
    return a + b

no1 = add(1,2)
no2 = add(10,134)

print('no1 : ', no1)
print('no2 : ', no2)

duhagi = add

num1 = duhagi(10, 20)
num2 = duhagi(100, 10)

print('num1 : ', num1)
print('num2 : ', num2)

msg1 = add('black','pink')
print('msg1: ', msg1)

list1 = add([1, 2, 3], [4, 5, 6])
print('list1 : ', list1)

'''
# 들여쓰기를 하지 않으면 절대로 안됨
def fun1():
실행문 .....
'''


def func01(a, b='pink'):
    return a + b

group1 = func01('black')
print(group1)


group2 = func01('black', 'blue')
print(group2)