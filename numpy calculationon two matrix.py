import numpy as np
n=int(input())
m=int(input())
a=list(map(int,input().split()))
a2=np.array(a)
b=list(map(int,input().split()))
b2=np.array(b)
print(np.add(a2,b2),np.subtract(a2,b2),np.multiply(a2,b2),np.floor_divide(a2, b2),np.mod(a2,b2),np.power(a2,b2))

