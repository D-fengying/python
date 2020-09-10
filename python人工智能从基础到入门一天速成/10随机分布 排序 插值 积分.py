import numpy as np
import matplotlib.pyplot as mp
#随机分布：某人投篮命中概率为0.3，投10次进，3个球的概率
a = np.random.binomial(10, 0.3, 10000)
print('P(3)=',(a == 3).sum() / 10000)
#排序：
names = np.array(['a', 'b', 'c', 'd', 'e']) #商品名称
prices = np.array([100, 300, 200, 250, 150]) #价格
volumes = np.array([10, 9, 8, 7, 6])         #销量
indices = np.lexsort((volumes, prices))      #排序
print(names[indices])         #按价格排名输出
#插值
import scipy.interpolate as si
min_x = -50
max_x = 50
x = np.linspace(min_x, max_x, 13)
y = np.sinc(x)
mp.scatter(x, y, s=60, color='blue', marker='o')
mp.plot(x, y)
linear = si.interp1d(x, y, kind='cubic')
linear_x = np.linspace(min_x, max_x, 1000)
linear_y = linear(linear_x)
mp.plot(linear_x, linear_y, color='red')
mp.show()
#积分
def f(x):
    return 3*x**2 + x + 1
a, b= -5, 5
import scipy.integrate as si
r = si.quad(f, a, b)
print(r)
