# file: test04.py

a = 1
a = a + 1

a += 1

print('a : ', a)

c, d = 3, 4
print('c ~ d : ', c, ' - ', d)

e = 3.14;
f = 3.1415  # ==>  한 행에 두개 이상의 표현식을 나열할 경우에는 ; 을 구분자로 나열한다.
print('e : ', e);
print('f : ', f)
'''
    데이터를 두변수에서 서로 치환해야 하는 경우
    자바의 경우
        int a = 120;
        int b = 300;

        ==>
        int tmp = a;
        a = b;
        b = tmp;

    파이썬의 경우는 
        a = 10
        b = 20

        a, b = b, a 
'''

a, e = e, a

print('a : ', a)
print('e : ', e)

# b = c + d
# a = (b = c + d) # ==> b = c + d 가 표현식이 아니고 문장으로 해석해서 생기는 오류...

print()
print('type of 1 : ', type(1))
