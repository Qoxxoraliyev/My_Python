# Transport vositalari: Vehicle sinfi yaratib, 
# speed() metodini qo‘shing. Car va Bicycle sinflari ushbu 
# metodni o‘ziga xos tarzda amalga oshirsin.
class Vehicle():
    def __init__(self,name,year):
        self.name=name
        self.year=year
    def speed(self):
        print(f"{self.name} ning tezligi:80 km/h")
class Car(Vehicle):
    def __init__(self, name, year):
        super().__init__(name, year)
    def speed(self):
        print(f"{}")