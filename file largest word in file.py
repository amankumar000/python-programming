f=open(r"C:\Users\Abhishek\Desktop\info.py\info.txt","r")
data=f.read()
l=list(data.split())
max=len(max(l,key=len))
for i in l:
    if len(i)==max:
        print(i)
f.close()