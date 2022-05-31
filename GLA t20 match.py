r,o,c=map(int,input().split())
overlft=20-o
maxrun=overlft*36
totalruns=maxrun+c
if totalruns>r:
    print("yes")
else:
    print("no")