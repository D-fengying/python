import numpy as np
a = [1, 2, 3, 4, 5]  #源数组
b = [3, 2, 1]        #卷积核数组
c = np.convolve(a, b, 'full')   #完全卷积 长度a+b-1
d = np.convolve(a, b, 'same')   #同维卷积 长度a
e = np.convolve(a, b, 'valid')  #有效卷积 长度a-b+1
print(c)
print(d)
print(e)