 
import numpy as np
r,c = map(int,input().split())
m1 = []
m2 = []
for i in range(r):
    ele = list(map(int,input().split()))
    m1.append(ele)
for i in range(r):
    ele = list(map(int,input().split()))
    m2.append(ele)
n1 = np.array(m1)
n2 = np.array(m2)

print(np.add(n1,n2))
print(np.subtract(n1,n2))
print(np.multiply(n1,n2))
print(np.floor_divide(n1,n2))
print(np.mod(n1,n2))
