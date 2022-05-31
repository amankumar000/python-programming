l1=[]
l2=[]
d={}
n=int(input("enter the size of list"))
print("enter the elements of list 1")

for i in range(n):
    l1.append(input())
print("enter the elements of second list")
for i in range(n):
    l2.append(input())
for i in range(n):
    d[l1[i]]=l2[i]

print(d)