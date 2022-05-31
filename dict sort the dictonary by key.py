d={}
d1={}
l=[]
n=int(input("enter the size of dictionary"))
for i in range(n):
    x,y=input("name") , input("roll no")
    d[x]=y
for i in d:
    l.append(i)
l.sort()
print("dictonary before  sort",d)
for i in l:
    c=d.get(i)
    d1[i]=c
print(f"dictonary after sort{d1}")




