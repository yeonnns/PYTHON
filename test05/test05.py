# file: test05.py

'''
    구구단 5단 출력

dan = 5;
gop = 1;
while gop < 10:
    print('{0}  x {1} = {2}'.format(dan, gop, dan * gop))
    gop += 1
'''

'''
    1~9단 출력
dan = 2;

while dan < 10:
    gop = 1;
    while gop < 10:
        print('{0}  x {1} = {2}'.format(dan, gop, dan * gop))
        gop += 1
    dan += 1
print('-----------------------')

'''

dan = 2
i = 0
while i < 2:
    gop = 1
    while gop < 10:
        j = 0
        result = ''
        while j < 4:
            result += '{0}  x {1} = {2}\t\t'.format(dan + j, gop, dan * gop)
            j += 1
        gop +=1
        print(result)
    print()
    dan = 6
    i += 1