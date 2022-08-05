#file: test03.py

class MyException(Exception):
    def __init__(self, args):
        super().__init__('정수가 아닙니다.: {0}'.format(args))

def convert_to_integer(text):
    if text.isdigit():
        return int(text)
    else:
        raise MyException(text)

if __name__ == '__main__':
    try:
        print('숫자를 입력하세요.')
        text = input()
        number = convert_to_integer(text)
    except MyException as err:
        print('예외발생 : [ {0} ]'.format(err))
    else:
        print('정수형식으로 변환됐습니다. : {0}({1})'.format(number, type(number)))
print('프로그램종료')