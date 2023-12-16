num=int(input("enter the number"))
flag=False
if(num==1):
    print("not prime no")
elif(num>1):
    for i in range(2,num):
        if(num%i==0):
            flag=True
            break
if flag:
    print("not prime")
else:
    print("prime")                