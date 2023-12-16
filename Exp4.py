print("Sharan Shetty 60004220224")
try:
    int_value = int(input("Enter Number:"))
except ValueError as ve:
    print(f"Caught ValueError: {ve}")

try:
    numer = int(input("Enter Numerator:"))
    denom = int(input("Enter Denominator:"))
    result = numer / denom
    print(result)
except ZeroDivisionError as zererr:
    print(f"Caught ZeroDivisionError: {zererr}")

try:
    a_list = [1, 2, 3, 4, 5]
    print(a_list)
    i = int(input("Enter index:"))
    print(a_list[i])
except IndexError as ie:
    print(f"Caught IndexError: {ie}")

try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as fnfe:

    print(f"Caught FileNotFoundError: {fnfe}")

try:
    import nonexistent_module
except ModuleNotFoundError as e:
    print(f"Caught ModuleNotFoundError: {e}")


class AgeOfMinorException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

age = int(input("Enter Age to cast vote:"))

try:
    if age < 18:
        raise AgeOfMinorException("You cannot vote. Your Age is less than 18 and you are a Minor")
    else:
        print("You can vote.")
except AgeOfMinorException as ageex:
    print(f"Caught AgeOfMinorException: {ageex.message}")
