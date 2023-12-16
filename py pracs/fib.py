n=int(input("enter n"))

def fib(n):
    if(n==1):
        print(1)
    else:    
        a=0
        b=1
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(n)