a=5
b=2

try:
    print("Resource Opened")
    print(a/b)
    k=int(input("enter a number"))
    print(k)
except ZeroDivisionError as e:
    print("cannot divide by 0")
except ValueError as e:
    print("invalid input")
except Exception as e:
    print("something is wrong")

finally:
    print("process finished")            

