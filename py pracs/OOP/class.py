
# class
class Computer:
    # method
    def config(self):
        print("i5,16gb")

comp1=Computer()
print(type(comp1))        

Computer.config(comp1)

# or

comp2=Computer()
comp2.config()
