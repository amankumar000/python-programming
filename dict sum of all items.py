n=int(input("enter the size of dict"))
d={}
for i in range(n):
    x,y=input("enter the key"),int(input("enter the value"))
    d[x]=y
s=0
for i in d:
    c=d.get(i)
    s=s+c
print("the sum of items of dict",s)