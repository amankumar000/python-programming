n=int(input("enter the size of dict"))
d={}
for i in range(n):
    x,y=input("enter the key"),input("enter the value")
    d[x]=y
s=''
d2={}
for i in d:
    if i not in s:
        d2[i]=d.get(i)
        s=i
print(d2)
