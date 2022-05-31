n=int(input())
for i in range(n):
    l=list(map(int,input().split()))
    if l[0]+l[2]==180:
        if l[1] + l[3] ==180:
            print('YES')
    else:
        print("NO")
