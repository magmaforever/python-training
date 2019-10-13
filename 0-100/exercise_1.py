# 打印水仙花数

for num1 in range(100, 1000):
    low = num1 % 10
    mid = num1 // 10 % 10
    high = num1 // 100
    if num1 == low**3 + mid**3 + high**3:
        print(num1)

# 正整数的反转

num2 = int(input('num2 = '))
rev_num2 = 0
while num2 > 0:
    rev_num2 = rev_num2 * 10 + num2 % 10
    num2 //= 10
print(rev_num2)

# 百钱百鸡问题

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡：%d只，母鸡：%d只，小鸡：%d只' % (x, y, z))
