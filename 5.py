class Kvadrat():
    def __init__(self,a,b=2):
        self.a=a
        self.b=b
    def perimetrni_top(self):
        print(f"{self.a*2}")
obj=Kvadrat(4,8)
obj.perimetrni_top()
class Tortburchak(Kvadrat):
    def perimetrni_top(self):
        return f"{2*(self.a*self.b)}"
    def yuza(self):
        return {self.a}*{self.b}
    