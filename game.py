import random
a=[]
i=0
print("enter the size of list")
n=int(input())
print("enter the elements in the list")
while(i<n):
    a.append(int(input()))
    i=i+1
print("enter any number from the list")
print(a)
b=int(input())
c=random.choice(a)
s=int(input("enter the number of chances"))
if(b==c):
    print("you won the game","\U0001F920")
elif b not in a:
        print("Choose the correct number from list")
else:
    if c<b:
        print("too high","\U0001F915")
        print(f"""correct no. is{c}""")

    elif c>b:
        print("too low","\U0001F637")
        print(f"""correct no. is{c}""")
