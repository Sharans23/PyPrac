print("Sharan Shetty 60004220224 C151 C3-1")

l=[]
n = int(input("Enter length of list: "))

for i in range(n):
    a = int(input("Enter element: "))
    l.append(a)
print(l)

oddnos=list(filter(lambda x: x%2!=0,l))
cube=list(map(lambda x: x**3,oddnos))
print("Answer ",cube)
