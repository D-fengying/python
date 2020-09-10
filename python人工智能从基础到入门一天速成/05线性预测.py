import numpy as np

a = [1, 2, 3, 4, 5, 6]       #给出的前6个数字
A = np.zeros((3, 3))
for j in range(3):
    A[j, ] = a[j:j+3]
print(A)
B = a[3: 6]
x = np.linalg.lstsq(A, B)[0]
print(x)
print(np.dot(B, x))