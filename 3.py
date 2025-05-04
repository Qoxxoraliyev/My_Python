class Algebra():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        print(f"Ikki sonning yig'indisi:{self.a+self.b}")
class Matem(Algebra):
    def sum(self):
        print(f"Ikki sonning ko'paytmasi:{self.a*self.b}")
c=Matem(6,8)
c.sum()