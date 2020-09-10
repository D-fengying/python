import numpy as np
#矩阵求逆
m = np.mat('3 4 5;5 4 3;4 5 3')
print(m)
print(m.I)  #求逆矩阵
m_inv = np.linalg.inv(m)
print(m_inv)
print(m * m.I)  #原矩阵与逆矩阵相乘是单位矩阵

#解方程 ：假设有若干大人和小孩去春游，去的时候是
#坐大巴大人票价是2元，小孩票价是1元，一共花了20
#回去坐的是火车大人票价3元，小孩票价是2元，一共花了35
#求大人和小孩有几人
A = np.mat('2 1; 3 2') #A矩阵为票价
B = np.mat('20; 35')  #B矩阵为消费
x = np.linalg.solve(A, B)
print(x)
#数组的裁剪与压缩
a = np.arange(1, 10)
print(a)
print(np.clip(a, 3, 7))#小于3部分都变3，大于7部分都变7
print(a.compress(a > 5)) #保留大于5的部分


