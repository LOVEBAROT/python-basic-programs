from array import *
arr= array('i',[])#empty array
n=int(input("enter array length"))

for i in range(n):
    x=int(input("enter value"))
    arr.append(x)
print(arr)
#first method for search
val=int(input("enter value for search"))
k=0
for e in arr:
    if(e==val):
        print(k)
        break
    k+=1

#second methon
print(arr.index(val))
