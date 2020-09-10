#回归计算中为什么不用循环而用向量计算
import numpy as np
import time
a = np.random.rand(100000)
b = np.random.rand(100000)
#for循环
c = 0
start = time.time()
for i in range(100000):
    c += a[i] * b[i]
end = time.time()
print("计算所用时间%s" % str(1000*(end - start)) + "ms")
print('-----\n \n \n')
#向量化计算
start = time.time()
c = np.dot(a, b)
end = time.time()
print("计算所用时间%s" % str(1000*(end - start)) + "ms")