class Uchish():
    def __init__(self,manzil,masofa):
         self.manzil=manzil
         self.masofa=masofa
         self.yoqigi=7000
    def yoqilgi_sarfi(self):
         print(f"Yoqilg'i {7000-(self.masofa*1000)/500} qoldi")
obj=Uchish("Turkiya",600)
obj.yoqilgi_sarfi()