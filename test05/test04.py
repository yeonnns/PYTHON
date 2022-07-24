# file: test04.py

data = enumerate((1, 2, 3)) # eunmerate() : 입력받은 데이터를 enumerate로 변환해주는 형변환
print('type : ', type(data))

print(data) #메모리 주소 찍어줌 , 열거타입

for i, v in data :
    print(i, '-', v)

black = {1: '제니', 2: '리사', 3: '로제', 4: '지수'}
en1 = enumerate(black)
for i, v in en1:
    print(i, '-', v)
    print('###', black[v])










