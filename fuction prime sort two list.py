def isprime(num):
    c=0
    for i in range(1,num):
        if num%i==0:
            c=c+1
    return c==1
st=eval(input())
list1=[]
list2=[]
for i in st:
    if isprime(int(i)):
        list1.append(i)
    else:
        list2.append(i)
list1.sort()
list2.sort()
k=list1+list2
out="".join(k)
print(f"'{out}"'')