n=int(input("enter the size of phonebook"))
p={}
for i in range(1,n+1):
    x,y=input("enter name"),input("enter the mobile number")
    p[x]=y
b=input("enter the name to search")
for i in p:
    m=p.get(b)
    if m:
        print(f'{b}:{m}')
        break
    else:
        print("mobile number not found")