# file: test04.py

'''
def printArg(a, *arg):
    print(a, ' - ', arg)

printArg(10)
printArg(10,20,30,40,50,60)
'''

def printf(format, *arg):
    print(format % arg)

printf('%d - %s', 1, 'jennie')
#printf('%d - %s', 'jennie', 1)

# 재귀함수
# n부터m까지 합을 구해주는 함수
def sumN(n, m):
    if n>m:
        n,m = m,n
    if m == n:
        return n
    return m + sumN(n,m-1)

print(sumN(1, 10))

# 문제 n 부터 m 까지 곱을 변환해주는함수

def gopN(n,m):
    if n>m:
        n,m = m,n
    if n == m:
        return m
    return m * gopN(n,m-1)

print(gopN(1, 3))