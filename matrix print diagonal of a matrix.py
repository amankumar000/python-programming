r=int(input("enter the size of rows"))
c=int(input("enter the size of columb"))
lst=[]

print("enter the elements of first matrix")
for i in range(r):
    l=[]
    for j in range(c):
        l.append(int(input("Enter the element : ")))
    lst.append(l)
z=[]
for i in range(r):
    for j in range(c):
        if i==j:
            print(lst[i][j],end='')

        else:
            print("  ",end='')
    print()