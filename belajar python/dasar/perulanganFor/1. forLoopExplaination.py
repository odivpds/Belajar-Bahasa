# 1. 
# Program ini akan menampilkan setiap karakter dalam variabel 'name' secara berurutan,
# sehingga nama akan ditampilkan secara vertikal / menurun satu karakter per baris.
name = "Putu Agus Prana Dhiva Satvika"
for item in name:
    print(item)
print("\n")  # Mencetak baris kosong untuk memberikan jarak antara operasi.


numbers = [1, 2, 3, 4, 5, 6]

# Program ini akan mengalikan setiap angka dalam list 'numbers' dengan 5 dan mencetak hasilnya.
for item in numbers:
    print(item * 5)
print("\n")  # Mencetak baris kosong untuk memberikan jarak antara operasi.



# 2.
# forLoop in range digunakan untuk mencetak perulangan angka dalam suatu range atau jarak tertentu, misalnya :
# Mencetak angka dari 0 hingga 4 (tidak termasuk 5).
for angka in range(5):
    print(angka)

# Mencetak angka dari 2 hingga 8 (tidak termasuk 9) dengan selisih 2.
for angka in range(2, 9, 2):
    print(angka)
    
# Program ini akan mencetak angka dari 1 hingga 9 (tidak termasuk 10) dengan selisih 2
# Jadi, akan mencetak 1, 3, 5, 7, dan 9.
for i in range(1, 10, 2): #(angka start, angka finish, angka selisih)
    print(i)




