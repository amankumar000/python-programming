def info(lst):
    a = []

    for i in lst:
        if i not in a:
            a.append(i)

    return a


n = int(input())
lst = []
for i in range(1, n + 1):
    lst.append(int(input()))
print(info(lst))
