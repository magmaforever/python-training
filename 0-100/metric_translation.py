# 英制和公制转换

v = float(input('请输入长度：'))
unit = input('请输入单位(英寸in或厘米cm))：')
if unit == 'in' or unit == '英寸':
    print('%.10f英寸 = %.10f厘米' % (v, v * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%.10f厘米 = %.10f英寸' % (v, v / 2.54))
else:
    print('请输入有效的单位！')
