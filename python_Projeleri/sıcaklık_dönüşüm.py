# SICAKLIK DÖNÜŞÜM 

s = int(input("Sıcaklık değeri girin: "))
if s < -459.67:
    print("Tanımlamayan sıcaklık")
c = (s-32)/1.8000
print("Hava" , c , "Celcius olarak hesaplandı")
if 15 > c: 
    print("Hava soğuktur")
elif 25 > c > 16:
    print("Hava ılıktır")
elif c > 25: 
    print("Hava sıcaktır")