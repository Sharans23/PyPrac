class FiveDivisionError(Exception):
    pass

try:
    n1=int(input("enter no1"))
    n2=int(input("enter no2"))
    if n2==5:
        raise FiveDivisionError("cannot divide by five")
    div=n2/n1
    print("div is",div)

except (FiveDivisionError,ZeroDivisionError) as var:
    print(var)

    
