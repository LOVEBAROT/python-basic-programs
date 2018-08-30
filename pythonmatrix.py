from numpy import *
arr1=array([1,2,3,4,5])
arr1=arr1+5
print(arr1)
print(log(arr1))
arr1[1]=10
print(arr1)
print(id(arr1))

#matrix operation in py
arr2=array([[1,2,3],[4,5,6]])
print(arr2)

print(arr2.dtype)

print(arr2.ndim)

arr3=arr2.flatten()
print(arr3)

m=matrix(arr1)#matrix in python
print(m)

print(diagonal(m))

m1=matrix('1,2,3;4,5,6;1,6,7')
m2=matrix('2,3,4;1,2,3;6,9,4')
print(m2)
m3=m2+m1
print(m3)#matrix addition
