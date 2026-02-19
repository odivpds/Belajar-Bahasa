# Ini adalah definisi dari sebuah fungsi bernama 'perkalian'.
# Fungsi ini menerima dua parameter, 'a' dan 'b', dan mengembalikan hasil perkalian dari kedua parameter tersebut.
def perkalian(a, b):
    hasil = a * b  # Hasil perkalian dari 'a' dan 'b' disimpan dalam variabel 'hasil'.
    return hasil  # Fungsi mengembalikan nilai 'hasil' sebagai hasil perkalian.

# Menggunakan input dari pengguna untuk mendapatkan dua angka integer, 'Angka1' dan 'Angka2'.
# Kemudian, fungsi 'perkalian' dipanggil dengan kedua angka ini sebagai argumen,
# dan hasilnya disimpan dalam variabel 'result'.
result = perkalian(int(input("Angka1: ")), int(input("Angka2: ")))

# Hasil perkalian yang diperoleh dari fungsi 'perkalian' dicetak ke layar.
print(result)
