# iki boyutlu bir matrisi list comprehension yöntemi ile nasıl oluştururuz
rows, cols = 3, 4
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
print(matrix)


# Kullanıcıdan alınan verilerle matris oluşturan kod 

satir = int(input("Sütun sayısı giriniz -> "))
sutun = int(input("Satır sayısı giriniz -> "))
s_s1 = input("Matrix'e yerleştirmek istediğiniz sayıyı giriniz -> ")
matrix = [[s_s1 for i in range(satir)] for j in range(sutun)]
print(matrix)

# 0 matris oluşturan kod 

satir2 = int(input("Sütun sayısı giriniz -> "))
sutun2 = int(input("Satır sayısı giriniz -> "))
matrix2 = [[0 for i in range(satir2)] for j in range(sutun2)]
print(matrix2)




satir = int(input("Sütun sayısı giriniz -> "))
sutun = int(input("Satır sayısı giriniz -> "))
matrix = []

for i in range(sutun):
    row = []
    for j in range(satir):
        deger = input(f"Matrix'in ({i+1},{j+1}) konumuna yerleştirmek istediğiniz sayıyı giriniz -> ")
        row.append(deger)
    matrix.append(row)

print(matrix)