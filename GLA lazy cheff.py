n=int(input())
for i in range(n):
    x,m,d=map(int,input().split())
    l=x*m
    k=x+d
    print(min(l,k))
