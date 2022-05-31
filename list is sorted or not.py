def check(lst):
    c=sorted(lst)
    if c==lst:
        return True
    else:
        return False

n= int(input("enter the size of list"))
lst=[]
for i in range(n):
    lst.append(int(input("enter the elements")))

print(check(lst))

