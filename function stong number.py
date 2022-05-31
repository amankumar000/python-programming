import math
x=input("input the number")
def stong(x):

    s=0
    for i in x:
        s=s+math.factorial(int(i))
    if s==int(x):
        return "number is stong "
    else:
        return " not stong"
print(stong(x))
