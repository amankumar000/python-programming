a=int(input("enter the number"))
c=0
i=2
while(i<a):
    i=i+1
    if (a%i==0):

        c=c+1
if (c==1):
    print("entered numeber is prime")
else:
    print("enterd number is not prime")
