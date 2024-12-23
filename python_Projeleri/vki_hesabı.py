# Boy-Kilo indeksi hesaplayan algoritma Vücut kitle endeksi formül  VKİ = kg/boy*boy 
# 18.5 altı zayıf 18.5-24.9 normal 25-29.9 hafif kilolu 30-34.9 fazla kilolu +35 obez

boy = float(input("Lütfen boyunuzu giriniz -> "))
kilo = float(input("Lütfen kilonuzu giriniz -> "))
ikv = kilo/boy**2
if ikv < 18.5:
    print("zayıfsın")
elif 19 < ikv < 24.9:
    print("kilon normal")
elif 25 < ikv < 29.9:
    print("kilolusun")
elif 30 < ikv < 34.9:
    print("Kilon fazla")
elif 35 < ikv:
    print("Obezsin")