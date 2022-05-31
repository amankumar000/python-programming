students={}
n=int(input("enter the number of students"))
for i in range(1,n+1):
    x,y=input("enter the name "),int(input("enter the roll number"))
    marks=[]
    for j in range(5):
        mark=float(input("enter the marks"))
        marks.append(mark)
        students[x,y]=marks
print(students)
b=0
for i in students:
    s=0
    c=students.get(i)
    v=max(c)
    if b<v:
        b=v
        print(f"maximum marks  of={i} which is={v}")

