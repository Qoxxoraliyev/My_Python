# Foydalanuvchi kiritgan so‘z palindrom ekanligini tekshiruvchi dastur yozing
n=input().split()
if n[::-1]==n:
    print("Palindrom")
else:
    print("Palindom emas")