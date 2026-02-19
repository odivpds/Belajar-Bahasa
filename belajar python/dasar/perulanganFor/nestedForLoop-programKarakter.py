# Impor modul os untuk membersihkan layar konsol dengan os.system("cls").
import os
os.system("cls")  # Membersihkan layar konsol (hanya berfungsi di Windows).

# Menampilkan pesan kepada pengguna.
print("Program Tampil Karakter")

# Meminta pengguna untuk memasukkan karakter yang akan ditampilkan.
k = str(input('Masukkan karakter: '))

# Meminta pengguna untuk memasukkan jumlah baris yang ingin ditampilkan.
i = int(input("Masukkan jumlah baris: "))

# Loop pertama, mengatur jumlah baris yang akan ditampilkan.
for a in range(1, i + 1): # (angka start, angka finish + 1)
    # Loop kedua, mengatur jumlah karakter pada setiap baris.
    for j in range(1, a + 1):
        print(k, end="")  # Mencetak karakter 'k' tanpa baris baru.
    print()  # Mencetak baris kosong untuk pindah ke baris berikutnya.

# Loop kedua, mengatur jumlah baris yang akan ditampilkan secara terbalik.
for a in reversed(range(1, i + 1)):
    # Loop ketiga, mengatur jumlah karakter pada setiap baris secara terbalik.
    for j in reversed(range(1, a + 1)):
        print(k, end="")  # Mencetak karakter 'k' tanpa baris baru.
    print()  # Mencetak baris kosong untuk pindah ke baris berikutnya.

