# method overloading is two classes havving same name with different number of parameters

# method overloading is not possible but
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else:
            return a
        
s1=Student(87,89)
print(s1.add(2,3,1))
print(s1.add(2,3))

# method overriding
class A:
    def show(self):
        print("in A")

class B(A):
    pass

a1=B()
a1.show()