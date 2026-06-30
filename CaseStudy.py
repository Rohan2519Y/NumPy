import numpy as np

# 4 ====================================================================
#   A ##################################################################
zero = np.zeros(10)



#   B ##################################################################
vowel = np.array(['a', 'e', 'i', 'o', 'u'])



#   C ##################################################################
ones = np.ones([2, 5], dtype=int)



#   D ##################################################################
myarray1 = np.array([[2.7, -2, -19], [0, 3.4, 99.9], [10.6, 0, 13]])



#   E ##################################################################
# myarray2 = np.array(np.arange(4, 41, step=4, dtype=float).reshape(3, 3))
myarray2 = np.array(np.arange(4, 61, step=4, dtype=float).reshape(3, 5))







# 5 ====================================================================
#   A ##################################################################
# print("Dimension :", myarray1.ndim, myarray2.ndim)
# print("Shape :", myarray1.shape, myarray2.shape)
# print("Size :", myarray1.size, myarray2.size)
# print("Data Type :", myarray1.dtype, myarray2.dtype)
# print("Item Size Zero :", zero.itemsize)
# print("Item Size Vowel :", vowel.itemsize)
# print("Item Size Ones :", vowel.itemsize)
# print("Item Size myarray1 :", myarray1.itemsize)
# print("Item Size myarray2 :", myarray2.itemsize)



#   B ##################################################################
# print(ones.reshape(10))



#   C ##################################################################
# print(vowel[[2, 3]])



#   D ##################################################################
# print(myarray1[[1, 2]])



#   E ##################################################################
# print(myarray1)
# print(myarray1[:, [0, 1]])



#   F ##################################################################
# print(myarray1)
# print(myarray1[1:3,0])



#   G ##################################################################
# print(np.sort(vowel)[::-1])








# 6 ====================================================================
#   A ##################################################################
# print(ones / 3)



#   B ##################################################################
# print(myarray1 + myarray2)



#   C ##################################################################
# subarray = myarray2 - myarray1
# print(subarray)



#   D ##################################################################
# print(myarray1 * myarray2)



#   E ##################################################################
# myarray3 = myarray1 @ myarray2
# print(myarray3)



#   F ##################################################################
# print(myarray2 / myarray1)



#   G ##################################################################
# print((myarray1 ** 3)/2)



#   H ##################################################################
# print(np.round((myarray2 ** 2)/2, 2))







# 7 ====================================================================
#   A ##################################################################
# print(np.transpose(ones),'\n' , np.transpose(myarray2))



#   B ##################################################################
# print(np.sort(vowel)[::-1])



#   C ##################################################################
# print(myarray1)
# print(np.sort(myarray1, axis=0))






# 8 ====================================================================
#   A ##################################################################
# print(myarray2)
splt = np.split(myarray2, [1, 2, 3, 4], axis=1)
myarray2A = splt[0]
myarray2B = splt[1]
myarray2C = splt[2]
myarray2D = splt[3]
myarray2E = splt[4]
# print(myarray2A)
# print(myarray2B)
# print(myarray2C)
# print(myarray2D)
# print(myarray2E)



#   B ##################################################################
splt = np.split(zero, [2, 5, 7, 8])
zeroA = splt[0]
zeroB = splt[1]
zeroC = splt[2]
zeroD = splt[3]
# print(zeroA)
# print(zeroB)
# print(zeroC)
# print(zeroD)



#   C ##################################################################
# print(np.concatenate([myarray2A, myarray2B, myarray2C], axis=1))







# 9 ====================================================================
myarray4 = np.arange(-1 , 9.5, step=0.25).reshape(14, 3)
# print(myarray4)







# 10 ====================================================================
#   A ##################################################################
# print(np.sum(myarray4))



#   B ##################################################################
# print(np.sum(myarray4, axis=1))



#   C ##################################################################
# print(np.sum(myarray4, axis=0))



#   D ##################################################################
# print(np.max(myarray4))



#   E ##################################################################
# print(np.min(myarray4, axis=1))



#   F ##################################################################
# print(np.mean(myarray4, axis=1))



#   G ##################################################################
# print(np.std(myarray4, axis=0))








# Case Study -----------------------------------------------------------
File = np.loadtxt("F:/NumPy/iris.data", dtype=str, delimiter=',')
# print("Sepal Length\tSepal Width\tPetal Length\tPetal Width\tIris")
# for i in File:
#     print(f'{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t{i[3]}\t\t{i[4]}\t')



#1 ##################################################################
iris = np.array(File)
# print(iris)



#2 ##################################################################
iris = np.delete(iris, 4, axis=0)



#3 ##################################################################
# print(np.shape(iris), np.ndim(iris), np.size(iris))



#4 ##################################################################
splt = np.split(iris, [49, 99])
iris1 = splt[0]
iris2 = splt[1]
iris3 = splt[2]



#5 ##################################################################
# print(iris1)
# print(iris2)
# print(iris3)



#6 ##################################################################
header = np.array(['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Species No.'])



#7 ##################################################################
# print(header)



#8 ##################################################################
iris_max = np.max(iris[:, :4].astype(float), axis=0)
iris_min = np.min(iris[:, :4].astype(float), axis=0)
iris_avg = np.round(np.mean(iris[:, :4].astype(float), axis=0), 2)
iris_std = np.round(np.std(iris[:, :4].astype(float), axis=0), 2)
# print("Max :", iris_max)
# print("Min :", iris_min)
# print("Avg :", iris_avg)
# print("Std :", iris_std)



#9 ##################################################################
iris1_max = np.max(iris1[:, :4].astype(float), axis=0)
iris2_max = np.max(iris2[:, :4].astype(float), axis=0)
iris3_max = np.max(iris3[:, :4].astype(float), axis=0)
# print("Max 1 :", iris1_max)
# print("Max 2 :", iris2_max)
# print("Max 3 :", iris3_max)

iris1_min = np.min(iris1[:, :4].astype(float), axis=0)
iris2_min = np.min(iris2[:, :4].astype(float), axis=0)
iris3_min = np.min(iris3[:, :4].astype(float), axis=0)
# print("Min 1 :", iris1_min)
# print("Min 2 :", iris2_min)
# print("Min 3 :", iris3_min)

iris1_avg = np.round(np.mean(iris1[:, :4].astype(float), axis=0), 2)
iris2_avg = np.round(np.mean(iris2[:, :4].astype(float), axis=0), 2)
iris3_avg = np.round(np.mean(iris3[:, :4].astype(float), axis=0), 2)
# print("Avg 1 :", iris1_avg)
# print("Avg 2 :", iris2_avg)
# print("Avg 3 :", iris3_avg)

iris1_std = np.round(np.std(iris1[:, :4].astype(float), axis=0), 2)
iris2_std = np.round(np.std(iris2[:, :4].astype(float), axis=0), 2)
iris3_std = np.round(np.std(iris3[:, :4].astype(float), axis=0), 2)
# print("Std 1 :", iris1_std)
# print("Std 2 :", iris2_std)
# print("Std 3 :", iris3_std)



#10 ##################################################################
sepalminlen = np.min(iris[:, 0].astype(float))
sepalminwidth = np.min(iris[:, 1].astype(float))
petalminlen = np.min(iris[:, 2].astype(float))
petalminwidth = np.min(iris[:, 3].astype(float))
# print(sepalminlen)
# print(sepalminwidth)
# print(petalminlen)
# print(petalminwidth)

sepalminlensetosa = np.min(iris[:49, 0].astype(float))
sepalminwidthsetosa = np.min(iris[:49, 1].astype(float))
petalminlensetosa = np.min(iris[:49, 2].astype(float))
petalminwidthsetosa = np.min(iris[:49, 3].astype(float))
# print(sepalminlensetosa)
# print(sepalminwidthsetosa)
# print(petalminlensetosa)
# print(petalminwidthsetosa)

sepalminlensetosaVericolor = np.min(iris[49:99, 0].astype(float))
sepalminwidthsetosaVericolor = np.min(iris[49:99, 1].astype(float))
petalminlensetosaVericolor = np.min(iris[49:99, 2].astype(float))
petalminwidthsetosaVericolor = np.min(iris[49:99, 3].astype(float))
# print(sepalminlensetosaVericolor)
# print(sepalminwidthsetosaVericolor)
# print(petalminlensetosaVericolor)
# print(petalminwidthsetosaVericolor)

sepalminlenVirginica = np.min(iris[99:, 0].astype(float))
sepalminwidthVirginica = np.min(iris[99:, 1].astype(float))
petalminlenVirginica = np.min(iris[99:, 2].astype(float))
petalminwidthVirginica = np.min(iris[99:, 3].astype(float))
# print(sepalminlenVirginica)
# print(sepalminwidthVirginica)
# print(petalminlenVirginica)
# print(petalminwidthVirginica)

# print("\t\tIris Setosa\tIris Versicolor\tIris Virginica")
# print("---------------------------------------------------------------")
# print(f"Sepal Length\t{sepalminlensetosa > sepalminlen}\t\t{sepalminlensetosaVericolor > sepalminlen}\t\t{sepalminlenVirginica > sepalminlen}")
# print(f"Sepal Width\t{sepalminwidthsetosa > sepalminwidth}\t\t{sepalminwidthsetosaVericolor > sepalminwidth}\t\t{sepalminwidthVirginica > sepalminwidth}")
# print(f"Sepal Length\t{petalminlensetosa > petalminlen}\t\t{petalminlensetosaVericolor > petalminlen}\t\t{petalminlenVirginica > petalminlen}")
# print(f"Sepal Length\t{petalminwidthsetosa > petalminwidth}\t\t{petalminwidthsetosaVericolor > petalminwidth}\t\t{petalminwidthVirginica > petalminwidth}")



#11 ##################################################################
sepalavgwidthsetosa = np.mean(iris[:49, 1].astype(float))
sepalavgwidthvirginica = np.mean(iris[99:, 1].astype(float))
# print(sepalavgwidthsetosa, sepalavgwidthvirginica)
# print(sepalavgwidthsetosa > sepalavgwidthvirginica)
# print(sepalavgwidthsetosa < sepalavgwidthvirginica)



#12 ##################################################################
petalavglensetosa = np.mean(iris[:49, 2].astype(float))
petalavglenvirginica = np.mean(iris[99:, 2].astype(float))
# print(petalavglensetosa, petalavglenvirginica)
# print(petalavglensetosa > petalavglenvirginica)
# print(petalavglensetosa < petalavglenvirginica)



#13 ##################################################################
petalavgwidthsetosa = np.mean(iris[:49, 3].astype(float))
petalavgwidthvirginica = np.mean(iris[99:, 3].astype(float))
# print(petalavgwidthsetosa, petalavgwidthvirginica)
# print(petalavgwidthsetosa > petalavgwidthvirginica)
# print(petalavgwidthsetosa < petalavgwidthvirginica)



#14 ##################################################################
# np.savetxt('F:/NumPy/IrisMeanValues.txt', iris_avg, delimiter=',', fmt = '%f')



#15 ##################################################################
# np.savetxt('F:/NumPy/IrisStat.txt', [iris_max, iris_avg, iris_min], delimiter=',', fmt = '%f')