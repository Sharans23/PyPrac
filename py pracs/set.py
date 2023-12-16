s1={1,2,3,4,5,6}
s2={1,2,3,8}
s3={2,3}

s2.add(9)
print(s2)

s1.pop()
print(s1)

print(s1.difference(s2))

s2.discard(9)
print(s2)

z=s3.issubset(s2)
print(z)
z=s2.issubset(s3)
print(z)

z=s3.issuperset(s2)
print(z)
z=s2.issuperset(s3)
print(z)

z=s1.union(s3)
print(z)
z=s1.intersection(s3)
print(z)
