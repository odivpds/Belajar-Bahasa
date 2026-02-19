# List berisi beberapa dictionary yang berisi informasi tentang buku-buku.
buku_buku = [
    {"judul": "Harry Potter", "pengarang": "J.K. Rowling", "tahun": 1997},
    {"judul": "To Kill a Mockingbird", "pengarang": "Harper Lee", "tahun": 1960},
    {"judul": "The Great Gatsby", "pengarang": "F. Scott Fitzgerald", "tahun": 1925},
    {"judul": "1984", "pengarang": "George Orwell", "tahun": 1949},
]

# Menggunakan perulangan for untuk mengakses setiap dictionary dalam list.
for buku in buku_buku:
    # Mengambil informasi buku dari setiap dictionary.
    judul = buku["judul"]
    pengarang = buku["pengarang"]
    tahun = buku["tahun"]
    
    # Melakukan operasi pada data buku.
    print(f"Judul: {judul}")
    print(f"Pengarang: {pengarang}")
    print(f"Tahun Terbit: {tahun}")
    
    if tahun < 2000:
        print("Buku ini adalah klasik.")
    else:
        print("Buku ini adalah buku modern.")
    
    print("\n")

# Setelah perulangan selesai, kita keluar dari perulangan.
print("Semua informasi buku telah ditampilkan.")
