n=int(input("enter size of dict"))
d={}
for i in range(n):
    x,y=input("enter the key"),int(input("enter the value"))
    d[x]=y
v=0
k=0
for i in d:
    c=d.get(i)
    if c>v:
        v=c
for j in range(0,n+1):
    l=d.get(d[j])
    s=d.get(d[j+1])
    if l<s:
        l=k

print(f"highest value is{v} and lowest value is {k}")