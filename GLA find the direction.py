n=int(input())
for i in range(n):
    l=list(map(int,input().split()))
    s=r=0
    for j in l:
        if j==0:
            r=r+1
        else:
            s=s+1
    if s>r:
        print("YES")
    else:
        print("NO")