lst=['abhishek','nikhil','mayannk']
print(sorted(lst,key=lambda x: sum(map(ord,x))))


