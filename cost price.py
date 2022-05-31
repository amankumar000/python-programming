d=[]
t=int(input())
for i in range(t):
    (a,b)=map(int,input().split())
    d.append(a%b)
for j in d:
    print(j)