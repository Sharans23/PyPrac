print("Sharan Shetty 60004220224 C151 C3-1")

n = int(input("Enter a number- "))


def check(n):
    sum = 0
    for i in range(1,n):
        if (n%i == 0):
            sum += i
            if (sum == n):
                return "Perfect Number"
    return False

print(check(n))
