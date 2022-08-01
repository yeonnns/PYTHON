# file: test01.py

'''
irum = 'jennie'

print(irum)
print('{0:10}'.format(irum)) # 기본값 왼쪽정렬
print('{0:<10}'.format(irum)) # 왼쪽 정렬
print('{0:>10}'.format(irum)) # 오른쪽 정렬
'''

'''
    문제 ]
        num = '12345'
        를 숫자로 변환해서 오른쪽 정렬


num = '12345'
num = int(num)
print(type(num))

result = '{0:>10}'.format(num)
print('{0:11} : {1}'.format('오른쪽 정렬 ', result))
print('{0:11} : {1}'.format('기본 왼쪽 정렬', num))
print('{0:>10}'.format(num))

'''

irum = 'jennie'
age = 27

print('{0} 의 나이는 {1} 입니다.'.format(irum, age))
print('%s 의 나이는 %d 입니다.' % (irum, age))
print('내년에는 {age} 살인 {0} 입니다.'.format(irum, age=28))

# 문자열.zfile(숫자) : 숫자만큼 공간 확보하고 앞부분 0으로 채움

irum = 'jennie'
irum = irum.zfill(15)
print(irum)