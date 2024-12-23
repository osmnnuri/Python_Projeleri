# q'ya basana kadar input alarak liste oluşturan ve listedeki min maks değeri yazdıran kod 

list = []

while True:
    x = input("Bir sayı giriniz. İşlemi sonlandırmak için q tuşuna basınız -> ")
    if x == "q":
        break
    list.append(x)
m = max(list)
n = min(list)
print(m,n)


# Hazır listeyi tersine çeviren kod

list = []

while True:
    d = input("Listeye eklemek istediğiniz değerleri giriniz -> ")
    if d == "q":
        break
for i in range(len(list)-1, -1, -1):
    list.append(d)
    
print(list)  

list = []

while True:
    y = input("Eklemek istediğiniz sayıyı giriniz -> ")
    if y == "q":
        break
    list.append(y)

ters_liste = []


# Kart tahmin oyunu

import random
kartlar = [ "Kız","Papaz","Juliet","1","2","3","4","5","6","7","8","9","10","As"]
hak = 0
pc = random.choices(kartlar)
while True:
    tahmin = input("Tahmininizi giriniz -> ")
    if tahmin == pc:
        print("TAHMİNİNİZ DOĞRU, KAZANDINIZ!")
        break
    if tahmin != pc:
        print("TAHMİNİNİZ YANLIŞ, TEKRAR DENEYİNİZ!")
    hak += 1
    if hak == 5:
        print("HAKKINIZ BİTMİŞTİR, KAYBETTİNİZ!")
        break


# Kelime Tahmin Oyunu

import random

kelimeler = ["elma", "bilgisayar", "dünyalilar", "radyasyon", "kahve", "masa", "güzel", "kitap", "otobüs", "çikolata",
"prizma", "kaktüs", "deniz", "gitar", "bulut", "kamera", "televizyon", "kaplumbağa", "fırça", "köprü",
"kale", "kelebek", "ördek", "dinozor", "uçak", "arı", "fare", "perde", "telefon", "araba"]
kelime = random.choice(kelimeler)
print(f"Kelimeniz {len(kelime)} harf uzunluğunda, 5 Hakkınız vardır. Bol Şans.")
hak = 0

while True:
    tahmin = input("Harf veya kelime giriniz -> ")
    if tahmin == kelime:
        print("BİLDİNİZ TEBRİKLER!")
        break
    if tahmin != kelime:
        print("TAHMİNİNİZ YANLIŞ")
        hak += 1
    if hak == 5:
        print("HAKLARINIZ TÜKENMİŞTİR, ADAM ASILDI GG")
        break