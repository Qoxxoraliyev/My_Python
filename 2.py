class Calculator():
      def __init__(self,a,b):
            self.a=a
            self.b=b
class Algebra(Calculator):
      def kopaytma(self):
            print(f"Ikki sonning kopaytmasi:{self.a*self.b}")
ab=Algebra(4,5)
ab.kopaytma()