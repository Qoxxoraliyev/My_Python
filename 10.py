# Foydalanuvchi kiritgan ikki son orasidagi 
# barcha tub sonlarni topuvchi dastur yozing.
a,b=map(int,input().split())
if a>b:
    for i in range(b,a+1):
        if a%i!=0 and a%i!=1:
            print(i)