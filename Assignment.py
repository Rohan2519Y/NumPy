import numpy as np

# 1 - How to create an empty and a full NumPy array?
# print(np.empty(5))
# print(np.full(5, 5))



# 2 - Create a Numpy array filled with all zeros
# print(np.zeros(5))



# 3 - Create a Numpy array filled with all ones
# print(np.ones(5))



# 4 - Check whether a Numpy array contains a specified row
# Arr = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
# Row = np.array([4, 5, 6])

# print(np.any(np.all(Arr == Row, axis = 1)))



# 5 - How to Remove rows in Numpy array that contains non-numeric values?
# Arr = np.array([
#     [1, 2, 3],
#     ['q', 'e', 'r'],
#     [7, 8, 9],
#     ['q', 'e', 'r']
# ], dtype=object)
# Arr1 = Arr.copy()
# for i in range(Arr.shape[0]-1, -1, -1):
#     for j in range(len(Arr[i])):
#         if isinstance(Arr[i][j], str):
#             Arr1 = np.delete(Arr1, i, axis=0)
#             break

# print(Arr1)


# 6 - Remove single-dimensional entries from the shape of an array
# Arr = np.array([[1, 2, 3]])
# print(np.squeeze(Arr))



# 7 - Find the number of occurrences of a sequence in a NumPy array
# Arr = np.array([1, 2, 3, 1, 2, 3, 1, 2, 3])
# seq = np.array([1, 2, 3])

# count = 0
# for i in range(len(Arr) - len(seq) + 1):
#     if np.array_equal(Arr[i:i+len(seq)], seq):
#         count += 1
# print(count)



# 8 - Find the most frequent value in a NumPy array
# Arr = np.array([1, 2, 4, 1, 2, 4, 2, 3, 4, 2])
# element, count = np.unique(Arr, return_counts=True)
# freq = dict(zip(element, count))
# print(max(freq, key=freq.get))



# 9 - Combining a one and a two-dimensional NumPy Array
# Arr1 = np.array([1, 2, 3, 4])
# Arr2 = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]).flatten()
# Arr = np.concatenate((Arr1, Arr2))
# print(Arr)



# 10 - How to build an array of all combinations of two NumPy arrays?
# Arr1 = np.array([1, 2, 3])
# Arr2 = np.array([4, 5])
# Mix = np.array(np.meshgrid(Arr1, Arr2)).T.reshape(-1, 2)
# print(Mix)



# 11 - How to add a border around a NumPy array?
# Arr = np.array([
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3]
# ])
# Border = np.pad(Arr, pad_width=1, mode='constant', constant_values=0)
# print(Border)



# 12 - How to compare two NumPy arrays?
# Arr1 = np.array([1, 2, 3])
# Arr2 = np.array([1, 2, 3])
# print(Arr1 == Arr2)
# print(np.array_equal(Arr1, Arr2))
# print(np.all(Arr1 == Arr2))
# print(np.any(Arr1 == Arr2))
# print(np.allclose(Arr1, Arr2))



# 13 - How to check whether specified values are present in NumPy array?
# Arr1 = np.array([1, 2, 3])
# print(1 in Arr1)



# 14 - How to get all 2D diagonals of a 3D NumPy array?
# Arr = np.array([
#     [[1,2,3],
#      [4,5,6],
#      [7,8,9]],

#     [[10,11,12],
#      [13,14,15],
#      [16,17,18]]
# ])

# print(np.diagonal(Arr, axis1=1, axis2=2))



# 15 - Flatten a Matrix in Python using NumPy
# Arr = np.array([
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3]
# ])
# print(Arr.flatten())



# 16 - Flatten a 2d numpy array into 1d array
# Arr = np.array([
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3]
# ])
# print(Arr.flatten())



# 17 - Move axes of an array to new positions
# Arr = np.arange(24).reshape(2, 3, 4)
# print(np.moveaxis(Arr, 0, 2))



# 18 - Interchange two axes of an array
# Arr = np.arange(24).reshape(2, 3, 4)
# print(np.moveaxis(Arr, 0, 2))



# 19 - Counts the number of non-zero values in the array
# Arr = np.array([1, 2, 3, 4, 0, 4, 0, 4, 3, 7, 0])
# print(np.count_nonzero(Arr))



# 20 - Count the number of elements along a given axis
# Arr = np.array([
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3]
# ])
# print(Arr.shape)



# 21 - Trim the leading and/or trailing zeros from a 1-D array
# Arr = np.array([0, 1, 0, 2, 0])
# print(np.trim_zeros(Arr))



# 22 - Change data type of given numpy array
# Arr = np.array([1, 2, 3, 4, 5], dtype=float)
# print(Arr)



# 23 - Reverse a numpy array
# Arr = np.array([1, 2, 3, 4, 5])
# print(Arr[::-1])



# 24 - How to make a NumPy array read-only?
# Arr = np.array([1, 2, 3, 4, 5])
# Arr.flags.writeable = False
# print(Arr)



# 25 - Get the maximum value from given matrix
# Arr = np.array([
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3]
# ])
# print(np.max(Arr))



# 26 - Get the minimum value from given matrix
# Arr = np.array([
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3]
# ])
# print(np.min(Arr))



# 27 - Find the number of rows and columns of a given matrix using NumPy
# Arr = np.array([
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3]
# ])
# print(Arr.shape)



# 28 - Select the elements from a given matrix
# Arr = np.array([
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3]
# ])
# print(Arr[0][0])
# print(Arr[1:])



# 29 - Find the sum of values in a matrix
# Arr = np.array([
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3]
# ])
# print(np.sum(Arr))



# 30 - Calculate the sum of the diagonal elements of a NumPy array
# Arr = np.array([
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3]
# ])
# print(np.sum(np.diag(Arr)))



# 31 - Adding and Subtracting Matrices in Python
# Arr1 = np.array([
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3]
# ])
# Arr2 = np.array([
#     [4, 5, 6],
#     [4, 5, 6],
#     [4, 5, 6]
# ])
# print(Arr2 - Arr1)
# print(Arr2 + Arr1)



# 32 - Ways to add row/columns in numpy array
# Arr = np.array([
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3]
# ])
# RowArr = np.vstack([Arr, [1, 2, 3]])
# print(RowArr)
# ColArr = np.hstack([Arr, [[4], [4], [4]]])
# print(ColArr)



# 33 - Matrix Multiplication in NumPy
# Arr1 = np.array([
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3]
# ])
# Arr2 = np.array([
#     [4, 5, 6],
#     [4, 5, 6],
#     [4, 5, 6]
# ])
# print(Arr1 @ Arr2)



# 34 - Get the eigen values of a matrix
# Arr = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
# print(np.linalg.eig(Arr)[0])



# 35 - How to Calculate the determinant of a matrix using NumPy?
# Arr = np.array([
#     [1, 2, 3],
#     [6, 2, 6],
#     [7, 9, 9]
# ])
# print(np.linalg.det(Arr))



# 36 - How to inverse a matrix using NumPy
# Arr = np.array([
#     [1, 2, 3],
#     [6, 2, 6],
#     [7, 9, 9]
# ])
# print(np.linalg.inv(Arr))




# 37 - How to count the frequency of unique values in NumPy array?
# Arr = np.array([
#     [1, 2, 3],
#     [6, 2, 6],
#     [7, 9, 9]
# ])
# V, C = np.unique(Arr, return_counts=True)
# F = dict(zip(V.tolist(), C.tolist()))
# print(F)



# 38 - Multiply matrices of complex numbers using NumPy in Python
# A = np.array([[1+2j, 3+4j], [5+6j, 7+8j]])
# B = np.array([[2+1j, 4+3j], [6+5j, 8+7j]])
# print(A @ B)



# 39 - Compute the outer product of two given vectors using NumPy in Python
# A = np.array([1, 3, 5])
# B = np.array([2, 4, 6])
# print(np.outer(A, B))



# 40 - Calculate inner, outer, and cross products of matrices and vectors using NumPy
# A = np.array([1, 3, 5])
# B = np.array([2, 4, 6])
# print(np.inner(A, B))
# print(np.outer(A, B))
# print(np.cross(A, B))




# 41 - Compute the covariance matrix of two given NumPy arrays
# A = np.array([1, 3, 5])
# B = np.array([2, 4, 6])
# print(np.cov(A, B))



# 42 - Convert covariance matrix to correlation matrix using Python
# A = np.array([1, 3, 5])
# B = np.array([2, 4, 6])
# cov = np.cov(A, B)
# d = np.sqrt(np.diag(cov))
# corr = cov / np.outer(d, d)
# print(corr)



# 43 - Compute the Kronecker product of two mulitdimension NumPy arrays
# Arr1 = np.array([
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3]
# ])
# Arr2 = np.array([
#     [4, 5, 6],
#     [4, 5, 6],
#     [4, 5, 6]
# ])
# print(np.kron(Arr1, Arr2))



# 44 - Convert the matrix into a list
# Arr = np.array([
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3]
# ])
# Arr = Arr.tolist()
# print(Arr)