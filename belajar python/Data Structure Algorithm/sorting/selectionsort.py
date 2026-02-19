def selectionsort(angka):
    for tujuan in range(len(angka)-1,0,-1):
        max = 0
        for i in range (1, tujuan+1):
            max_temp = angka[max]
            if max_temp < angka[i]:
                max=i
        angka[max],angka[tujuan] = angka[tujuan], angka[max]
    return angka

angka = [56,3,17,49]

print("sebelum",angka)
selectionsort(angka)
print("sesudah",angka)