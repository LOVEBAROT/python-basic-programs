x=int(input("enter first no"))
y=int(input("enter second no"))
z=int(input("enter third no"))
if(x>y)and (x>z):
    print("x is max",x)
elif (y>z) and (y>x):
    print("y is max",y)
else:
    print("z is max",z)


