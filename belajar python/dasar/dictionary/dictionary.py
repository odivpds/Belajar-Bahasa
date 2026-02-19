# Membuat dictionary harus dengan kurung kurawal
user = {
    "name" : "Agus Prana",
    "age" : 20,
    "alamat" : "Manukaya Anyar"
}

# code untuk menampilkan data dari dictionary
data = user["name"], user["age"], user["alamat"]
print(data)


# function get digunakan untuk menghindari error jika data tidak terdapat di dalam dictionary.
data2 = user.get("username")
# output dari data2 akan = none, karena data yang di print tidak ada di dalam dictionary.
print(f"data2 adalah : {data2}")


# Pada fungsi get jika kita menambahkan string lagi dibelakang string "username" maka string tersebut yang akan di cetak.
data3 = user.get("username", "odivpds")
# output dari data3 adalah odivpds.
print(f"data3 adalah : {data3}")


#untuk menambahkan data yang tidak ada, kita dapat menggunakan code ini :
user["username"] = "Putu Agus Prana Dhiva Satvika"
# outputnya data4 akan mencetak username diatas biarpun username tidak tersedia di variable user.
data4 = user.get("username")
print(f"ternyata username dari data2 adalah {data4}")
