ls = []
n=int(input("enter the number of rows"))
print("enter the elements")
for i in range(n):
    ls1=[]
    for j in range(n):
        ls1.append(int(input()))
    ls.append(ls1)
print(ls)
for ele in ls:
    print(*ele)
