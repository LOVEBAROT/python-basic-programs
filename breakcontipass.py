av=3

x=int(input("how many candy you are require"))
i=1
while i<=x:
    if i>av:
        print("out of stock")
        break#break statement in python
    print("candy",i)
    i+=1
print ("bye")


for j in range(1,10):

    if j%3==0:
        continue#continue statement in python
    print(j)



