a=dict()
b={}
n=int(input("enter the size"))
for i in range(n):
    r,s=map(str,input().split())
    a[r]=s
print(a)
for i in a:
    x=i.upper()
    n=a.get(i)
    b[x]=n
print(b)