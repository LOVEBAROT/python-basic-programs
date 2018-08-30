x=int(input("how many row required..?"))
y=int(input("how many column required...?"))

for i in range(x):
    for j in range(y):
        print("*",end="")
    print()
print()
for i in range(4):
    for j in range(i+1):
        print("*",end="")
    print()
print()
for i in range(4):
    for j in range(4-i):
        print("*",end="")
    print()
print()
for i in range(4):
    for j in range(4-i):
        print(i+j+1,end="")
    print()

