def check(l):
    c=0
    for i in range(0,n):
        for j in range(i+1,n):
            if (l[i]+l[j])%k==0:
                c=c+1
    return c

l = []
n = int(input())
k=int(input("value of k"))
for i in range(n):
    l.append(int(input()))
print(check(l))