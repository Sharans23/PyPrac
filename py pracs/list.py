# list is mutable
name=["sharan","hello",2,4,1]
print(name[3])

name.append("me")
print(name)

name.insert(2,'sharan2')
print(name)

name.remove("sharan")
print(name)

name.pop(3)
print(name)

name.append(1)
print(name)

name.pop()
print(name)

del name[2:]
print(name)

name.extend([1,2,3,4,4,5])
print(name)

name.append([1,2,3,4])
print(name)

name1=[1,2,3,4,455,6,3,2,2,655,3]

print(min(name1))

print(max(name1))

name1.sort()
print(name1)