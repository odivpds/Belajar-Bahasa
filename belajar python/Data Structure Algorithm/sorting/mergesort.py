def mergesort(angka):
    jumlah = len(angka)
    if jumlah > 1:
        posisi_tengah = jumlah//2
        potong_kiri = angka [:posisi_tengah]
        potong_kanan = angka[posisi_tengah:]
        mergesort(potong_kiri)
        mergesort(potong_kanan)
        jumlah_kiri = len(potong_kiri)
        jumlah_kanan = len(potong_kanan)
        ctrl_all,ctrl_kiri,ctrl_kanan = 0,0,0
        while ctrl_kiri < jumlah_kiri or ctrl_kanan < jumlah_kanan:

            #elemen di potongan kiri habis
            if ctrl_kiri == jumlah_kiri:
                angka[ctrl_all] = potong_kanan[ctrl_kanan]
                ctrl_kanan = ctrl_kanan+1
            
            #elemen di potongan kanan habis
            elif ctrl_kanan == jumlah_kanan: 
                angka[ctrl_all] = potong_kiri[ctrl_kiri]
                ctrl_kiri = ctrl_kiri+1
            
            #membandingkan nilai elemen kiri lebih kecil dari kanan
            elif potong_kiri[ctrl_kiri] <= potong_kanan[ctrl_kanan]:
                angka[ctrl_all] = potong_kiri[ctrl_kiri]
                ctrl_kiri = ctrl_kiri+1
            
            #membandingkan nilai elemen kanan lebih besar dari kiri
            else:
                angka[ctrl_all] = potong_kanan[ctrl_kanan]
                ctrl_kanan = ctrl_kanan+1
            ctrl_all = ctrl_all+1

angka= [43,5,34,92,29,87,9]
print("sebelum",angka)
mergesort(angka)
print("sesudah",angka)