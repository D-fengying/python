#对于n阶方阵A，如果存在数a和非零n维向量b使得Ab=ab,
# 则称a是矩阵A的一个特征值，x为特征向量
import numpy as np
import scipy.misc as sc
import matplotlib.pyplot as mp
A = np.mat('2 4;3 5')
print(A)
#提取特征值
a, b = np.linalg.eig(A)
print(a) #特征值数组
print(b) #特征向量数组
#求原方阵
A2 = b * np.diag(a) * b.I
print(A2)
#图片还原
C = sc.imread('1.jpg',True)
print(C.shape)
C = np.mat(C)  #先变成矩阵
c, d = np.linalg.eig(C)  #提取特征值
re = d * np.diag(c) * np.linalg.inv(d)
mp.imshow(re.real,cmap='gray')
mp.xticks([])    #去坐标
mp.yticks([])
mp.tight_layout()
mp.show()

