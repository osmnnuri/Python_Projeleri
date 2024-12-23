# İKİ BASAMAKLI SAYILARDA SIRALAMA

p = int(input("Lütfen iki basamaklı bir sayı giriniz: "))
o = p//10
n = p - o*10
print(n)
print(o)

if n > o:
    print("Birler basamağı onlar basamağından büyüktür")
else:
    print("Onlar basamağı birler basamağından büyüktür")
