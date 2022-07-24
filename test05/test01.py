#file test.py

'''
# 튜플
ldata = ('jennie', 'risa', 'rose', 'jisoo')
print(len(ldata))
print(ldata+ldata+ldata)
print(ldata*3)
# ldata[0] = 100 튜플 변경 불가
print(ldata)

# 데이터를 변경시키는 방법
# 1. 리스트로 변환하고
tdata = list(ldata)
tdata[0] = 'JENNIE'
print(tdata)

ldate = tuple(tdata)

print('ldata : ', ldata)
'''

tmap = {
    1: 'jennie',
    2: 'lisa'
}

print(type(tmap))

key = tmap.keys()
print(key)

values = tmap.values()
print(values)

items = tmap.items()
print(items)
