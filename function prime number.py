x=int(input("enter the number"))
def prime(x):
    c=0
    for i in range (1,x):
        if x%i==0:
            c=c+1
    if c==1:
        return "number is prime number"
    else:
        return "number is not prime number"
print(prime(x))