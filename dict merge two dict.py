d1 = {}
n1 = int(input("enter the size of first dictionary"))
d2 = {}
n2 = int(input("enter the size of second dictionary"))
for i in range(n1):
    x, y = input("enter the key of first dict"), input("enter the value")
    d1[x] = y
for i in range(n2):
    c, d = input("enter the key of second dict"), input("enter the value")
    d2[c] = d
for i in d2:
    c = d2.get(i)
    d1[i] = c
print(d1)

