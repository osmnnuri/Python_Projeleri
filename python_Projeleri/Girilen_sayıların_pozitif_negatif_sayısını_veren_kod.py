# Girilen sayılarda pozitif negatif sayısını veren kod
pozitif = 0
negatif = 0
list = []
while True:
    sayi = input("Bir sayı giriniz: ")
    list.append(sayi)
    if sayi == "q":
        break
    if int(sayi) > 0:
        pozitif += 1
    if int(sayi) < 0:
        negatif += 1