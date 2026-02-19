def find_max(array, n):
    # basis untuk rekursi
    if n == 1:
        return array[0]
    else:
        # panggil fungsi secara rekursif untuk memperoleh nilai terbesar dari setengah bagian kiri array
        max_left = find_max(array, n // 2)
        # panggil fungsi secara rekursif untuk memperoleh nilai terbesar dari setengah bagian kanan array
        max_right = find_max(array[n // 2:], n - n // 2)
        # bandingkan nilai terbesar dari kedua setengah bagian array
        return max(max_left, max_right)

def find_min(array, n):
    # basis untuk rekursi
    if n == 1:
        return array[0]
    else:
        # panggil fungsi secara rekursif untuk memperoleh nilai terkecil dari setengah bagian kiri array
        min_left = find_min(array, n // 2)
        # panggil fungsi secara rekursif untuk memperoleh nilai terkecil dari setengah bagian kanan array
        min_right = find_min(array[n // 2:], n - n // 2)
        # bandingkan nilai terkecil dari kedua setengah bagian array
        return min(min_left, min_right)
    
array = [3, 3, 2, 8, 11, 9, 10]

max_value = find_max(array, len(array))
min_value = find_min(array, len(array))

print("Nilai terbesar:", max_value)
print("Nilai terkecil:", min_value)
