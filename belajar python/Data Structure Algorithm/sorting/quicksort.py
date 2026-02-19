#=============Program Quicksort Selalu Pilih Elemen Terakhir Sebagai Pivot=============


# Code fungsi untuk melakukan pertukaran elemen pada posisi yang ditentukan
def tukar(array, i, n):
    array[i], array[n] = array[n], array[i]

# Code fungsi untuk membagi array menjadi dua bagian dan mengembalikan indeks pivot
def partisipant(array, lower, higher):
    # Code untuk menggunakan elemen terakhir sebagai pivot
    pivot = array[higher]
    # Code Indeks untuk memisahkan elemen yang lebih kecil dari pivot
    i = lower - 1

    for n in range(lower, higher):
        # Code Jika elemen lebih kecil dari atau sama dengan pivot
        if array[n] <= pivot:
            # Melakukan pertukaran elemen
            i = i + 1
            tukar(array, i, n)

    # Code untuk penempatan pivot ke posisi yang tepat
    tukar(array, i + 1, higher)
    return i + 1

# Code fungsi utama QuickSort
def quicksort(array, lower, higher):
    if lower < higher:
        # Memperoleh indeks pivot setelah membagi array
        pivot_index = partisipant(array, lower, higher)

        # Memanggil quicksort untuk dua bagian array sebelum dan setelah pivot
        quicksort(array, lower, pivot_index - 1)
        quicksort(array, pivot_index + 1, higher)

# Code menjalankan program sorting
array = [84, 3, 11, 54, 29, 92, 4, 7, 65]
p = len(array)

print("Array sebelum diurutkan:")
print(array)

quicksort(array, 0, p - 1)

print("Array setelah diurutkan:")
print(array)