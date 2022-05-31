n=int(input())
l=[]
for i in range(n):
	a=input()
	l1=len(a)
	f=int(a[0])+int(a[l1-1])
	l.append(f)
for j in l:
	print(j)