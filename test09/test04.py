# file: test04.py

nums = [1, 3, 6, 3, 8, 76, 13, 23, 13, 2, 3, 3.14, 2, 3, 7]

def test1(n):
    assert type(n) is int, '정수 이외의 데이터가 있습니다.'

for i in nums:
    test1(i)