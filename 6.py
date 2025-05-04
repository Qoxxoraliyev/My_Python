# n-gacha bo‘lgan Fibonachchi sonlarini chiqaruvchi dastur yozing.
def find_fibonacci(n,ls):
    if n==1:
        return ls
    return ls(n-1)+ls(n-2)
n=int(input())
ls=[0,1]
print(ls)