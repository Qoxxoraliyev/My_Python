class Calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
class Algebra(Calculator):
    def sum(self):
        print(f"{self.a}+{self.b}={self.a+self.b}")
my_digit=Algebra(5,6)
my_digit.sum()