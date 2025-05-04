# Foydalanuvchi kiritgan matndagi har bir harf nechta 
# marta qatnashganini hisoblovchi dastur yozing.
text=input()
text1=list(set(text))
for j in range(len(text1)):
      if text1[j] in text:
        print(f"{text1[j]}:{text.count(text1[j])}")
