f1=open("a.txt","r")
f2=open("b.txt","a")
f2.write(f1.read())
f2.close()
f2=open("b.txt","r")
lines=f2.read()
print(lines)
f1.close()
f2.close()