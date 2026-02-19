def penjumlahan(a,b):
    rumus = a+b
    return rumus

def pengurangan(a,b):
    rumus = a-b
    return rumus

def perkalian(a,b):
    rumus = a*b
    return rumus

def pembagian(a,b):
    rumus = a/b
    return rumus


print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan_operasi =input("Masukan Operasi 1/2/3/4: ")
angka1 =int(input("Angka Pertama: "))
angka2 =int(input("Angka Kedua: "))

if pilihan_operasi =="1":
    print(f"{angka1} + {angka2} = {penjumlahan(angka1,angka2)}")

elif pilihan_operasi =="2":
    print(f"{angka1} - {angka2} = {pengurangan(angka1,angka2)}")

elif pilihan_operasi =="3":
    print(f"{angka1} * {angka2} = {perkalian(angka1,angka2)}")

elif pilihan_operasi =="4":
    print(f"{angka1} : {angka2} = {pembagian(angka1,angka2)}")
    
else:
    print("operasi tidak ditemukan :( ")




