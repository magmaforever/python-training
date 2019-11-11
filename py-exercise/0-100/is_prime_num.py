# 检查1到100里面所有的素数，并列出


def is_prime_num(input_num):
    inum = int(input_num)
    if inum == 1:
        return False
    else:
        for j in range(2, inum - 1):
            if inum % j == 0:
                return False
                break
        return True


for i in range(1, 100):
    if is_prime_num(i):
        print('%d是素数' % i)
