# Rastgele elemanlardan oluşan matris 
import random

m1 = [[0 for x in range(3)] for y in range(3)]
m2 = [[0 for x in range(3)] for y in range(3)]
mt = 0

for i in range(3):
    for j in range(3):
        m1[i][j] = random.randint(0,9)
        m2[i][j] = random.randint(0,9)
        mt = m1[i][j] + m2[i][j]

print(m1)
print(m2)
print(mt)

# Rastgele Sayılarla Matris Oluşturan Kod 
import random as rd

m1=[[rd.randint(0,9) for _ in range(3)] for _ in range(3)]
m2=[[rd.randint(0,9) for _ in range(3)] for _ in range(3)]
mt=[[m1[i][j]+ m2[i][j] for j in range(3)] for i in range(3)]
print("ilk matris (m1):")
for row in m1:
    print(row)
print("ikinci martis(m2)")
for row in m2:
    print(row)
print("toplam matrisler(mt)")
for row in mt:
    print(row)

    
# Matristeki en büyük-küçük değeri veren kod 
import random as rd

m1=[[rd.randint(0,100) for _ in range(3)] for _ in range(3)]
m2=[[rd.randint(0,100) for _ in range(3)] for _ in range(3)]
mt=[[m1[i][j]+ m2[i][j] for j in range(3)] for i in range(3)]
print("ilk matris (m1):")
for row in m1:
    print(row)
print("ikinci martis(m2)")
for row in m2:
    print(row)
print("toplam matrisler(mt)")
for row in mt:
    print(row)

a = max(m1)
b = min(m1)

print(f"m1 matrisinin en büyük değeri {a}, en küçük değeri {b}'dir.")

# girilen n değerine göre nxn bir matris oluşturan kod (chatgpt)

def matris_olustur(N):
    matris = []
    sayi = 1
    
    for i in range(N):
        satir = []
        for j in range(N):
            satir.append(sayi)
            sayi += 1
        matris.append(satir)
    
    return matris

# Kullanıcıdan N değerini alma
N = int(input("Matris boyutunu girin (N): "))

# Matris oluşturma ve yazdırma
matris = matris_olustur(N)
for satir in matris:
    print(satir)


# Referanssız Matris yapımı

import random as rd 
m1 = [[0 for x in range(3)] for y in range(3)]
m2 = [[0 for x in range(3)] for y in range(3)]

for i in range(3):
    for j in range(3):
        m1[i][j] = rd.randint(0,9)
        m2[i][j] = rd.randint(0,9)

print(f"{m1} matrisi")
print(f"{m2} matrisi")
