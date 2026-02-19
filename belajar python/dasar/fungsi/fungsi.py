# Contoh Penggunaan Fungsi
def insert():
    print("Hai Aku odiv")
    print("Senang bertemu dengan kalian")

print("Selamat Pagi Semuanya")
insert()
print("Terimakasi :)")


print("===============================")
print(" ")


def hello(name, asal,umur):
    print(f"Hallo perkenalkan nama saya {name}")
    print(f"Berasal dari {asal} dan")
    print(f"Umur saya adalah {umur} tahun")

print("Selamat pagi semuanya")
hello("Odiv","Tampaksiring", 19) # Pemanggilan variable juga bisa dengan cara menggunakan keyword argument seperti disamping ini --> hello(name="odiv", umur=19), jika variable umur di panggil duluan maka parameternya tidak akan kebalik.
print("Terimakasi")