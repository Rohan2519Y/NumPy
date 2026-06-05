# array
#   - ndim - Dimension
#   - shape - rows and columns
#   - size - rows * columns
#   - dtype - data type
#   - itemsize - size in byte of one element
# 
# 
# 
# 
# 
# 
# 


###########################################################################################

import numpy as np
# L = [1, 2, 3, 4, 5]
# L = [1, 2, 3, 4, 5, 'Gwalior']
# A = np.array(L)
# A = np.array(L, dtype=float)
# A = np.array(L, dtype = 'int64')
# print(L)
# print(A + 30)
# print(A)


# L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# A = np.array(L)
# print(A)


# L1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# L2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# A = np.array(L1)
# B = np.array(L2)
# print(A * B)
# print(A @ B)


L1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
L2 = [1, 2, 3]
A = np.array(L1)
B = np.array(L2)
# print(A.ndim)
# print(B.ndim)
# print(A.shape)
# print(B.shape)
# print(A.size)
# print(B.size)
# print(A.dtype)
# print(B.dtype)
# print(A.itemsize)
# print(B.itemsize)
print(A.itemsize)
print(B.itemsize)