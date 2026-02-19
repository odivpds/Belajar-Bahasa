def cari_minimal_maximal(arr, n):
    if n == 1:
        return (arr[0], arr[0])
    else:
        min_value, max_value = cari_minimal_maximal(arr, n-1)
        if arr[n-1] < min_value:
            min_value = arr[n-1]
        elif arr[n-1] > max_value:
            max_value = arr[n-1]
        return (min_value, max_value)

arr = [8, 5, 2, 2, 7, 6]
n = len(arr)

min_value, max_value = cari_minimal_maximal(arr, n)

print("Nilai terkecil dari array adalah:", min_value)
print("Nilai terbesar dari array adalah:", max_value)

