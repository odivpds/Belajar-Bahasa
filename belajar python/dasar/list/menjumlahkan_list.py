# program ini akan menjumlahkan semua list dengan perulangan for
numbers = [5,3,8,6,2,1,9]

angka = 0
for number in numbers:
    angka = angka + number

print(angka)



# penggunaan functions bawaan dari python :

# SUM digunakan untuk menjumlahkan semua list yang ada
angka = sum(numbers)
print(f"jumlah keseluruhan list adalah {angka}")


# MAX/MIN digunakan untuk memunculkan angka tertinggi/terendah yang ada dalam list :

angka = max(numbers)
print(f"angka tertinggi dalam list adalah {angka}")



# Cara lain untuk mencari max number : 
# 1. Menggunakan sort
numbers.sort()
max_number = numbers[-1]
print(max_number)


#2. Menggunakan perulangan for untuk memunculkan angka terendah
number_min = numbers[0]
for number in numbers:
    if number_min > number:
        number_min = number
print(number_min)
