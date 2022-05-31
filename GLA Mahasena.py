n=int(input())
l=list(map(int,input().split()))
c=0
m=0
for i in range(n):
    if l[i]%2==0:
        c=c+1
    else:
        m=m+1
if c>m:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
