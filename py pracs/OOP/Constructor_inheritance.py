class A:
    def __init__(self):
        print("in A")

    def feature1(self):
        print("feature 1-A is working")    

class B:
    def __init__(self):
        print("in B")
    def feature1(self):
        print("feature 1-B is working")        
    def feature2(self):
        print("feature 2-B is working")        

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C")

    def feat(self):
        super().feature2()    

c1=C()
c1.feature1()
c1.feat()

# Out only came as in A and in C because of MRO that follows left to right order and it is same in methods too
