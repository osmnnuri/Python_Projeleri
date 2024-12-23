# KARESEL ŞEKİL OLUŞTURMA

satir = int(input("Kaç satırdan oluşsun?: "))
sutun = int(input("Kaç sutündan oluşsun?: "))

for k in range(satir):
    for i in range(sutun):
        print("*", end=" ")
print()

# ÜÇGEN OLUŞTURMA 

for k in range(10, 0, -1):
    for i in range(k):
        print("*", end= " ")
    print()