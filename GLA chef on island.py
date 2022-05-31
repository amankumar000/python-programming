n=int(input())
for i in range(n):
    x,y,xr,yr,d=map(int,input().split())
    f = x//xr
    w =y //yr
    if (f <= w and f >= d):
        print("YES")
    elif (w <= f and w >= d):
        print("YES")
    else:
        print("NO")
