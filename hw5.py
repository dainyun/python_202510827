def read_single_digit(res):
    if res == 1:
        print('일', end = '')
    elif res == 2:
        print('이', end = '')
    elif res == 3:
        print('삼', end = '')
    elif res == 4:
        print('사', end = '')
    elif res == 5:
        print('오', end = '')
    elif res == 6:
        print('육', end = '')
    elif res == 7:
        print('칠', end = '')
    elif res == 8:
        print('팔', end = '')
    elif res == 9:
        print('구', end = '')
    else:
        print('영', end = '')


def read_number(num):
    read_single_digit(int(num[0]))
    read_single_digit(int(num[1]))
    read_single_digit(int(num[2]))



num = input('세 자리 정수 입력')
read_number(num)
