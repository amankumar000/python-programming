r=5
h=10
fr=15
a=int(input("enter the time"))
zz=fr*a
v=3.14*(r**2)*h

m=zz/(3.14*r**2)

if zz<v:
    print("UnderFlow")
    print(m)
    print(h-m)
if zz>v:
    print("OverFlow")
    print(zz-v)
elif(zz==v):
    print("tank is fully filled")