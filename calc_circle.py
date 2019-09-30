# 给定半径计算圆周长和面积

import math

r = float(input('请输入圆半径：'))
p = 2 * math.pi * r
area = math.pi * r * r
print('周长：%.2f' % p)
print('面积：%.2f' % area)
