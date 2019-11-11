# 这个库文件包含常用的函数，逐步增加


def leap_year(input_year):
    if input_year % 4 == 0 and input_year % 100 != 0:
        return True
    elif input_year % 400 == 0:
        return True
    else:
        return False


i = int(input('input year:'))
if leap_year(i):
    print('%d is leap year.' % (i))
else:
    print('%d is not leap year.' % (i))


def is_prime_num(input_num):
    inum = int(input_num)
    if inum == 1:
        return True
    else:
        for j in range(2, inum - 1):
            if inum % j == 0:
                return False
                break
        return True
