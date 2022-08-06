#file: test01.py

'''
class hello:
    num= 10

    @staticmethod
    def calc(x):
        return x + 10
'''

'''
h1 = hello()
h1.calc(20)

로 사용 해야 하지만 정적메소드 (@staticmethod) 이므로
인스턴스를 생성하지 않아도 사용할 수 있다.


print('hello.calc(20) : ',hello.calc(20))
'''

'''
class Test00:

    def __init__(self, no):
        self.no = no
    def printNo(self):
        print(self.no)

t1 = Test00(100)
t1.printNo() # 자바에서는 t1.printNo(t1)
'''

class hello:
    t = '상속 시켜주는 클래스'

    @classmethod
    def calc(cls):
        return cls.t

#hello 클래스를 상속받은 h2 클래스
class h2(hello):
    t = '상속 받은 클래스'

hh = h2()
hh.t = '나는 다른 클래스'

print(hh.calc())
print(hh.t)





