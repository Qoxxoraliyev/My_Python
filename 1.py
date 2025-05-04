# Hayvonlar sinfi: Animal nomli sinf yarating, 
# unda sound() metodi bo‘lsin. Ushbu sinfdan Dog va 
# Cat sinflarini meros qilib oling va sound() metodini
#  o‘ziga xos tarzda bajaradigan qiling.
class Animal():
    def __init__(self,name="ghgjh"):
        self.name=name
    def sound(self):
        print(f"{self.name} ning ovozi baland")
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print(f"{self.name} ning ovozi Miyov, Miyov")
cat=Cat("Olapar")
cat.sound()