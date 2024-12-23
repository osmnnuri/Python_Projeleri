# Taş Kağıt Makas -not oyun kullanıcı kazanana kadar devam ediyor-

import random

kullanici_skor = 0 
pc_skor = 0

while True:

    

    sayi = random.randint(1,3)

    kullanici = input("Ne oynayacağınızı seçiniz -> Tas/Kagıt/Makas -> ")
    
    if sayi == 1:
        print("Bilgisayar seçimi -> Makas")
    if sayi == 2:
        print("Bilgisayar seçimi -> Taş")
    if sayi == 3:
        print("Bilgisayar seçimi -> Kağıt")

    pc = sayi

    if kullanici == "Taş" and pc == 3:
        print("KAYBETTİNİZ ") 
        pc_skor += 1 
    if kullanici == "Makas" and pc == 2:
        print("KAYBETTİNİZ ") 
        pc_skor += 1 
    if kullanici == "Kağıt" and pc == 1:
        print("KAYBETTİNİZ ") 
        pc_skor += 1 
    if kullanici == "Taş" and pc == 1:
        print("KAZANDINIZ ") 
    kullanici_skor += 1 
    if kullanici == "Makas" and pc == 3:
        print("KAZANDINIZ ") 
        kullanici_skor += 1 
    if kullanici == "Kağıt" and pc == 2:
        print("KAZANDINIZ ") 
        kullanici_skor += 1 
    if kullanici == pc:
        print("BERABERE")
        
    if kullanici_skor or pc_skor == 3:
        break