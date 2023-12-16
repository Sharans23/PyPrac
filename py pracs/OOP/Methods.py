# Types of methods

class Student:

    school="SSA"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    @classmethod
    def get_school(cls):
        return cls.school
    
    @staticmethod
    def info():
        print("tp")

s1=Student(98,82,64)        
s1=Student(92,24,37)

print(s1.avg())

# class methods
print(Student.get_school())

# staticmethod
Student.info()