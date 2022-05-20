import numpy as np
n,m = map(int,input().split())
m1 = []

for i in range(n):
    k = list(map(int,input().split()))
    m1.append(k)
    
print(np.transpose(m1))

n = np.array(m1)

print(n.flatten())
