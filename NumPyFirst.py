# array
#   - ndim - Dimension
#   - shape - rows and columns
#   - size - rows * columns
#   - dtype - data type
#   - itemsize - size in byte of one element
#   - reshape - convert 1D to Multi Dimestional
#   - split - split the array in the multipart
#   - max - find the biggest element in the array or the matrix(row or column)
#   - min - find the smallest element in the array or the matrix(row or column)
#   - sum - sum element according to the rows or columns
#   - std - standard deviation
# 
# 
# 
# 
#    A @ B
#    A ** B
#    A / B
# 
# 
# 
# 
#   
# zeros - zero matrix
# ones - one matrix
# arrange - print elements from range
# transpose - interchange row and coluumn
# concatenate - merge the arrays
# mean - average
# median - center element
# savetxt - save file on the disk
# loadtxt - fetch data from the file
# 
# 
# 
# 
# 
# 
# 


###########################################################################################

import numpy as np
import streamlit as st
import math
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


# L1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# L2 = [1, 2, 3]
# A = np.array(L1)
# B = np.array(L2)
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



# A = np.zeros((3, 4), dtype = 'int64')
# B = np.arange(1,11)
# print(B)
# B = np.arange(1,11,2)
# print(B)
# L1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# L2 = [6,3,8,1,3,0,55,3,2,288,22,55,79]
# A = np.array(L1)
# B = np.array(L2)
# # print(A.transpose())
# A.sort()
# A.sort(axis = 0) #now sorting according to column by default sorting is row
# B.sort()
# print(A)
# print(B)




# L1 = [6,3,8,1,3,0,55,3,2,288,22,55,79]
# L2 = [6,3,8,1,3,0,55,3,2,288,22,55,79]

# L3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# L4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(np.concatenate((L1, L2)))
# print(np.concatenate((L3, L3), axis = 1))


# S = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
# print(S.reshape(1, 9))
# print(S.reshape(3, 3))
# print(S.reshape(9, 1))


# A = np.array([
#     [1, 2, 4, 5],
#     [1, 2, 4, 5],
#     [1, 2, 4, 5],
#     [1, 2, 4, 5],
#     [1, 2, 4, 5]
# ])

# print(np.split(A, [2]))
# print(np.split(A, [2, 3]))



# L1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# L2 = np.array([6,3,8,1,3,0,55,3,2,288,22,55,79])
# print(L1.max(axis = 0))
# print(L2.max())
# print(np.median(L2))


# Student = [[90,80,70],[95,40,20],[39,83,40]]
# S = np.array(Student)
# np.savetxt("F:/NumPy/student.csv", S, delimiter = ',', fmt = '%i', header = "RKVM Gwalior", footer = "1st year")
# S = np.loadtxt("F:/NumPy/student.csv", delimiter = ',')
# S = np.loadtxt("F:/NumPy/student.csv", skiprows = 1, delimiter = ',')
# print(S)


# House = [2,2,2,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,5,5,5,6,6,7,7,7,8,9,9,10]
# T = sorted(list(set(House)))
# D = {}
# for i in T:
#     D[i]=House.count(i) 

# for i in D:
#     print(i, ':', D[i])

# st.dataframe(D)



# House = [2,2,2,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,5,5,5,6,6,7,7,7,8,9,9,10]
# A = np.array(House)
# F = np.unique(A, return_counts=True)
# print(F)



# House = [2,2,2,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,5,5,5,6,6,7,7,7,8,9,9,10]
# T = sorted(list(set(House)))
# F = {}
# RF = {}
# for i in T:
#     F[i] = House.count(T)
#     RF[i] = round((House.count(i) / len(House)) * 100, 2)

# for i in F:
#     print(i, ':', F[i])
# for i in RF:
#     print(i, ':', RF[i])

# st.dataframe(D)


# House = [2,2,2,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,5,5,5,6,6,7,7,7,8,9,9,10]
# A = np.array(House)
# F = np.unique(A, return_counts=True)
# NM = F[0]
# FR = F[1]
# S= FR.sum()
# RF = FR/S
# print(RF)
# PRF = RF*100
# print(PRF)
# CRF = np.cumsum(FR)
# CRF = np.cumprod(FR)
# print(CRF)


# N = np.array([25, 26, 32, 37, 40])
# Mean = np.mean(N)
# K = N - Mean
# S = np.sum(K*K)
# print(S)
# ST = S/len(N)
# print(ST)
# SQRT = math.sqrt(ST)
# print(round(SQRT, 2))
# print(np.std(N))

# N = np.array([10, 10, 10, 15, 15, 18, 18, 18, 18, 18, 20, 20, 20, 20, 20, 20, 20, 20, 25, 25])
# N = np.array([30, 30, 90, 160, 50])
# Mean = np.mean(N)
# print(Mean)
# K = N - Mean
# S = np.sum(K*K)
# print(S)
# ST = S/len(N)
# print(ST)
# SQRT = math.sqrt(ST)
# print(round(SQRT, 2))
# print(np.std(N))


X = np.array([4, 8, 12, 16])
Y = np.array([5, 10, 15, 20])
Xsum = np.sum(X)
Ysum = np.sum(Y)
print('Sum of X :', Xsum)
print('Sum of Y :', Ysum)
Xsqr = np.sum(X * X)
Ysqr = np.sum(Y * Y)
print('Square of X :', Xsqr)
print('Square of Y :', Ysqr)
XY = np.sum(X * Y)
print("XY :", XY)
R = (len(X) * XY - (Xsum * Ysum))/ (math.sqrt((len(X) * Xsqr - (Xsum * Xsum)) * (len(X) * Ysqr - (Ysum * Ysum))))
print('R :', R)