class Computer:

    # class variable
    wheel=4
    def __init__(self):
        # instance variable
        self.name="pravin"
        self.age=18

    def update(self):
        self.age=30

c1=Computer()
c2=Computer()
print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)
print(c1.wheel)
print(c2.wheel)

c1.name="sharan"
c1.age="19"
print(c1.name)
print(c1.age)

c2.update()
print(c2.name)
print(c2.age)

# changes for every object
Computer.wheel=5
print(c1.wheel)
print(c2.wheel)