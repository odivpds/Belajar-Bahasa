# Program penggunaan dictionary, mengubah angka menjadi kata
numbers = (input("masukan angka: "))

numbers_mapping = {

    "1" : "Satu",
    "2" : "Dua",
    "3" : "Tiga",
    "4" : "Empat",
    "5" : "Lima",
    "6" : "Enam",
    "7" : "Tujuh",
    "8" : "Delapan",
    "9" : "Sembilan",
    "0" : "Nol",
}

output = "" # value dari output ini adalah kosong agar nantinya dapat ditambahkan variable ubah_angka
for i in numbers:
    ubah_angka = numbers_mapping.get(i, "invalid") # jika user tidak menginput number maka hasilnya invalid

    output += ubah_angka  + " " # "" adalah spasi

print(output)