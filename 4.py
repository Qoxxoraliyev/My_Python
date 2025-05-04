class Kvadrat():
    def __init__(self,a,b=2):
        self.a=a
        self.b=b
    def perimetrni_top(self):
        print(f"{self.a*2}")
obj=Kvadrat(5,6)
obj.perimetrni_top()