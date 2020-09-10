import numpy as np
import matplotlib.pyplot as mp
#协方差  用来判断两组数据相似程度 值为正表示正相关
# 值为负表示负相关 值越大表示相关程度越大
a = [20, 24, 27, 19, 15, 22, 13]
b = [18, 22, 25, 17, 14, 20, 10]
#平均值
ave_a = np.mean(a)
ave_b = np.mean(b)
#离差:样本点与平均值距离
dev_a = a - ave_a
dev_b = b - ave_b
#协方差：离差之积的平均值
cov_ab = np.mean(dev_a * dev_b)
print(cov_ab)
#相关系数：协方差除去两组统计样本标准差乘积是一个在【-1,1】之间的数
k = cov_ab/(np.std(a) * np.std(b))
print(k)
#多项式拟合
x = [1, 2, 3, 4, 5, 6, 7]
y = a
w = np.polyfit(x, y, 4)   #获取多项式系数
print(w)
z = np.polyval(w, x)      #通过多项式系数x向量求得y向量
mp.plot(x, z, color='red', label='Polyfit')
mp.legend()
#平滑处理
q = np.arange(1, 7, 0.01)
p = -0.25378788 * q**4 + 4.25505051 * q**3 -24.70833333 * q**2 +55.71139971 * q - 15.71428571
mp.plot(q, p)
mp.show()