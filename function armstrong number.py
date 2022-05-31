x=input("enter the number")
def arm(x):
    s=0
    l=len(x)
    for i in x:
        s=s+int(i)**l
    if s==int(x):
        return " Number is armstrong"
    else:
        return " not armstrong"
print(arm(x))