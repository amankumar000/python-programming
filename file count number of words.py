f=open(r"C:\Users\Abhishek\Desktop\info.py\info.txt","r")
data=f.read()
l=list(data.split())
c=0
for i in l:
    c=c+1
print("number of words in the file are:",c)
f.close()