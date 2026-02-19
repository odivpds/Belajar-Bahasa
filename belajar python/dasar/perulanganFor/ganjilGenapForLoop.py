# Impor modul os untuk mengakses fungsi sistem operasi.
import os

# Menggunakan os.system("cls") untuk membersihkan layar konsol. Ini berfungsi berbeda pada berbagai sistem operasi.
os.system("cls")

# Menampilkan pesan awal kepada pengguna.
print("PROGRAM TAMPIL ANGKA GENAP DAN GANJIL")

# Meminta pengguna untuk memasukkan nilai awal (start) dan nilai akhir (finish) dalam rentang angka.
a = int(input("Masukan Start : "))
b = int(input("Masukan Finish: "))

# Menggunakan loop for untuk iterasi melalui semua angka dalam rentang dari 'a' hingga 'b' (inklusif).
for i in range(a, b+1): # penggunaan "plus" pada parameter b untuk memunculkan angka Finish karena index dalam pemrograman dimulai dari angka 0

    # Mengecek apakah angka saat ini ('i') adalah ganjil atau genap.
    if i % 2 == 1: # % adalah sisa pembagian dari suatu bilangan, misal 5 % 2 = 1, 3 % 2 = 1, dan 10 % 4 = 2
        print(i, ": GANJIL")
    else:
        print(i, ": GENAP")

# numbers = [1,2,3,4,5]
# result = [num * 2 for num in numbers
#           if num % 2 == 0]
# print(result)