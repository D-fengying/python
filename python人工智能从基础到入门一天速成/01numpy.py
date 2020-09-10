import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
a.shape = (2, 3)  # 维度改为2行3列
print('a=',a)

b = np.arange(1, 10)#相当于输出数组
print('b=',b)

c = np.zeros(10)
print('c=',c)

d = np.ones((2,3))
print('d=',d)

e = np.arange(1, 19)
e.shape = (3, 2, 3)
print('e=',e)
print('e的第1页第2行第1列的元素是：',e[0][1][0])

f = np.arange(1, 10)
print('f=',f)
print('前三个元素：',f[:3])
print('倒序排序：',f[::-1])
print('从第二个元素开始间隔3',f[1::3])

a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)
print(a, '--> a')
print(b, '--> b')
# 水平方向操作
g = np.hstack((a, b))
print(g, '--> g')
a, b = np.hsplit(g, 2)
print(a, '--> a')
print(b, '--> b')