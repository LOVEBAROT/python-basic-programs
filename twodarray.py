from numpy import *
print("using simple array")
arr=array([1,2,3,5,7,9.0])
print(arr.dtype)
print(arr)

arr1=array([41,235,6.5],int)
print(arr1)
print("first method using linespace method")
arr3=linspace(0,20,dtype=int)
print(arr3)
print("using arange function")
arr4=arange(1,20,2)
print(arr4)
print("using logspace function")
arr5=logspace(1,4,num=5)
#print('%.2f'%arr5[2])
print(arr5)
print("using ones function its print all ones")
arr6=ones(3,int)
print(arr6)
print("using zeros function its print all zeros")
arr7=zeros(3,int)
print(arr7)
