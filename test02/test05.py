# file: test05.py

a = [1, 2, 3]  # ==> 리스트
b = [10, a, 30]  # ==> [10, [1, 2, 3], 30]
c = ['x', a, 'y']  # ==> ['x', [1, 2, 3], 'y']

print('a : ', a)
print('b : ', b)
print('c : ', c)

'''
    int[][] num = new int[5][];

    이라고 배열을 만들게 되면
    num 배열에는 배열만 입력할 수 있게된다.
        num[0] = {1, 2};
        num[2] = {10, 20, 30};
'''