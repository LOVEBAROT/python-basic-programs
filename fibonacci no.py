a=0
b=1
n=int(input("enter no of series to be generated"))
if n<=0:
    print("not possible")
    pass
elif n==1:
    print(a)
    pass
elif n>=2:
    print("{},{}".format(a,b),end='')
for i in range(2,n):
    c=a+b
    print(",{}".format(c),end='')
    a=b
    b=c


