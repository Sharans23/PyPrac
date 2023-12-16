class Computer:
    # it is a constructor
    def __init__(self,cpu,ram):
        print("in init")
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("Config is",self.cpu,self.ram)

comp1=Computer('i5',8)
comp2=Computer('i7',16)

comp1.config()
comp2.config()
