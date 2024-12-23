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

# Dizinin elemanlarını isteğe bağlı değiştirme (ÇALIŞMADI -VERİ HATASI-)

d = []
while True:
    dizi = input("Diziye eklemek istediğiniz sayıyı giriniz, işleminiz bitince q'ya basınız -> ")
    if dizi == "q":
        break
    if dizi != "q":
        d.append(dizi)
print(d)
x = input(f"{len(d)} elemanlı dizinin kaçıncı elemanını değiştirmek istiyorsunuz? -> ")
a = input("Belirlediğiniz eleman yerine geçmesini istediğiniz elemanı giriniz -> ")
d.insert(x,a)
print(d)