#file: test03.py

def func01(a):
    a = 'abcd'

b = 'efg'

func01(b)


print(b)

def func02(l):
    l[0] = 1

l1 = [10, 20, 30]

func02(l1)
print(l1)