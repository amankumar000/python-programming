a=int(input())
l=[]
l2=[]
for i in range(a):
    l=list(map(int,input().split()))
    m=max(l)
    l.remove(m)
    m2=max(l)
    l2.append(m2)
    del (l)
for j in l2:
    print(j)
