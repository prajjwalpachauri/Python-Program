f=open("yt1.txt",'r')
str=f.read()
print(str)
f.close()
h=open("yt.txt",'w')
h.write(str)
h.close()