# 计算三条边是否可以组成三角形，若是可以，计算三角形面积

a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a+b > c and a+c > b and b+c > a:
    print('周长: %.1f' % (a+b+c))
    p = (a+b+c)/2
    area = (p*(p-a)*(p-b)*(p-c)) ** 0.5
    print('面积: %.1f' % (area))
else:
    print('不构成三角形。')
