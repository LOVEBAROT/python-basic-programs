def isPrime(n):
    if n<2:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
no=int(input("enter no:"))
if isPrime(no):
    print(no,"is prime no")
else:
    print(no,"is not a prime no")