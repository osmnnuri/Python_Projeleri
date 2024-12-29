# 10luk tabanı 2lik tabana dönüştürme 

ikilik = ""
sayi = int(input("Bir sayı giriniz -> "))
orijinal_sayi = sayi  

while sayi != 0:
    ikilik = str(sayi % 2) + ikilik  
    sayi = sayi // 2

print(f"{orijinal_sayi} sayısının ikilik (binary) karşılığı -> {ikilik}")


# 10luk tabanı 2lik tabana dönüştürme DEF  

def binary(sayi):
    ikilik = ""
    
    while sayi != 0:
        ikilik = str(sayi % 2) + ikilik  
        sayi = sayi // 2
    return ikilik

sayi = int(input("Bir sayı giriniz -> "))
orijinal_sayi = sayi 
ikilik = binary(sayi)
print(f"{orijinal_sayi} sayısının ikilik (binary) karşılığı -> {ikilik}")