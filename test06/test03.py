#file: test03.py

'''
    리스트     : [데이터, 데이터, 데이터, ....]
    튜플      : (데이터, 데이터, .....)
    사전      : {키값:데이터, 키값:데이터, ....}
'''
'''
no = [1, 2, 3]
print(type(no))
for num in no:
    print(num)
else:
    print('실행종료!')

no = tuple(no)
print(type(no))
for num in no:
    print(num)
else:
    print('꺼내기종료!!!')
'''

# print('여기는 출력함수', end='#종료!')
'''
d1 = {'jennie': '제니', 'lisa': '리사', 'rose':'로제', 'jisoo': '지수'}
for k in d1: # 키값 출력
    print(k)

for k in d1 :
    print(d1[k])
print('*'*30)
for k in d1:
    print('{0:10} - {1:10}'.format(k, d1[k]))
    print('%-10s : %-10s' % (k, d1[k]))
'''
'''
list1 = [(no * 2 ) for no in range(1, 6)]
print(list1)

# 1부터 10사이에 정수중 홀수만 리스트로 만들어서 출력

list2 = [no for no in range(1, 11) if no % 2 == 1]
print(list2)
'''

list1 = [i * j for i in range(2, 10)
        for j in range(1, 10)]
print(list1)
print()
for i in range(0, len(list1)):
    print('{:3d}'.format(list1[i]), end='') #print() end='\n' 이 기본값으로 셋팅 되어있다.
    if(i + 1)%9 == 0:
        print()

