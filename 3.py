# Korporativ xodimlar: Employee sinfi yarating, unda 
# xodimning ismi va maoshi bo‘lsin. Manager va Developer 
# sinflarini meros qilib olib, ularga maxsus bonus tizimini qo‘shing.
class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def bonus(self):
        print(self.salary)
        print(f"{self.name} ning ish xaqi 15% ga oshirildi:{self.salary*1.15}")
class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def bonus(self):
        print(self.salary)
        print(f"{self.name} ning is haqi 20% ga oshirildi:{self.salary*1.20}")
Ali=Manager("Ali",15000)
Ali.bonus()
Vali=Developer("Vali",18000)
Vali.bonus()