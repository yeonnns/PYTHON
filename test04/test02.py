#file : test02.py
'''
msg = 'Black Pink'
# msg[6] = 'p'
print(msg)
'''

'''
# 리스트[] mutable 자료
blackpink = ['jennie', 'lisa', 'rose', 'jisoo']
blackpink[0] = 'Jennie'
print(blackpink)

# 튜플() immutable 자료
pink = ('jennie', 'lisa', 'rose', 'jisoo')
# pink[0] = 'Jennie' Tuple 은 변경 불가능한 자료형이므로 에러 발생
print(pink)

numList = [1, 2, 3]
print('type of numList : ', type(numList))
print('length of numList : ', len(numList))
print('numList 첫번째 데이터: ', numList[0])
print('numList 마지막 데이터: ', numList[-1])
print('numList 0부터 1 데이터', numList[0:2])
print(numList*5)

'''


'''
# range()
r = range(10)
print(r)
rList = list(r) # 형변환 함수, range 객체를 리스트로 형변환
print(rList)

tmp = []
for no in range(10):
    tmp += [no]
print(tmp)

# range(시작데이터:마지막데이터-1:증가값)

#구구단 2단을 출력
dan = 2
for gop in range(1, 10):
    print(dan, 'X ', gop, '=', dan*gop)

# 구구단 출력
for dan in range(2, 10):
    for gop in range(1, 10):
        print(dan, 'X ', gop, '=', dan*gop)
    print()



t = (1, 2, 3)
print(t)
print(t*5)

t += (4, 5, 6)
print(t)

# t[0] = 10 ==> 튜플은 데이터의 변경이 불가능한 자료구조, 덧붙이는건 가능

print(10 in t)

'''



'''
# d = {키:[벨류1, 벨류2,.....], 키:벨류, 키:벨류}

dic = {'blackpink' : ['jennie', 'lisa', 'rose', 'jisoo'], '소방차':['정원관', '김태형', '도건우']}

print(dic['blackpink'])
print(dic['소방차'])
print(dic['blackpink'][0])

for memb in dic['blackpink']:
    print(memb)

for memb in dic['소방차']:
    print(memb)

for key in dic:
    for memb in dic[key]:
        print(memb)
    print()
'''

'''
# 구구단을 2단과 5단을 사전에 기억시키고 하나씩 꺼내서 출력하세요

dan = (2, 5)

result = {dan[0]: [], dan[1] : []}

for d in dan :
    r = d * 10
    for no in range(d, r, d):
        result[d] += [no]

print(result)
print()
for d in result:
    print('# ', d, '단')
    gop = 1;
    for no in result[d]:
            print(d, ' x ', gop, ' = ', no)
    print()
'''
dan = (2, 5)
result = {dan[0]: {}, dan[1] : {}}
for key in result:
    for gop in range(1, 10):
         result[key][gop] = key * gop;

print(result)
for d in result:
    print('---', d, '단')
    for gop in result[d]:
        print(d, 'x', gop, '=', result[d][gop])
    print()
