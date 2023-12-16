# for writting
f1=open('write.txt','w')
f1.write("Hello  ")

# for appending
f1=open('write.txt','a')
f1.write("hello guys")

#reading
f=open('tp.txt','r')
# print(f.read())

f2=open('tp2.txt','w')
for data in f:
    f2.write(data)


f3=open('tp2.txt','r')
print(f3.read())