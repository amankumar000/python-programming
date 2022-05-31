n = int(input("enter the size of dict"))
d = {}
v = {}
for i in range(n):
    x, y = input("enter the key"), int(input("enter the value"))
    d[x] = y
s = 0
m = int(input("enter multiple of"))
for i in d:
    c = d.get(i) * m
    v[i] = c

print("dict after the multiply in items", v)