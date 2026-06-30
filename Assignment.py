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