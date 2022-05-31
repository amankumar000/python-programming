r=int(input("enter the size of rows"))
c=int(input("enter the size of columb"))
lst=[]
lst2=[]
print("enter the elements of first matrix")
for i in range(r):
    l=[]
    for j in range(c):
        l.append(int(input("Enter the element : ")))
    lst.append(l)
print("enter the elements of second matrix")
for i in range(r):
    l=[]
    for j in range(c):
        l.append(int(input("Enter the element : ")))
    lst2.append(l)

out=[[0]*c for i in range(r)]
for i in range(r):
    for j in range(c):
        out[i][j] = lst[i][j] + lst2[i][j]

for k in out:
    print(*k)