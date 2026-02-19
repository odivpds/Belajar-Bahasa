# Program kalkulator sederhana menggunakan Python

# Fungsi penjumlahan
def add(x, y):
    return x + y

# Fungsi pengurangan
def subtract(x, y):
    return x - y

# Fungsi perkalian
def multiply(x, y):
    return x * y

# Fungsi pembagian
def divide(x, y):
    return x / y

# Tampilan menu operasi
print("Pilih operasi.")
print("1.Penjumlahan")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")

# Meminta input dari user
choice = input("Masukkan pilihan(1/2/3/4): ")

num1 = float(input("Masukkan angka pertama: "))
num2 = float(input("Masukkan angka kedua: "))

# Proses sesuai pilihan yang dipilih
if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Input salah")
