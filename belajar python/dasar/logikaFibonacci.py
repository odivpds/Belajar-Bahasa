fibo=[0, 1] # angka start
for i in range(2, 10):
  angka1 = fibo[i - 2] 
  angka2 = fibo[i - 1]
  angkaSelanjutnya = angka1 + angka2 # mencetak angka selanjutnya

  fibo.append(angkaSelanjutnya)
  
print(fibo)

# fibo = [0, 1]: Ini adalah inisialisasi list fibo dengan dua elemen pertama dari urutan Fibonacci, yaitu 0 dan 1. Ini adalah angka-angka awal yang digunakan untuk memulai perhitungan.

# for i in range(2, 10): Ini adalah loop for yang akan menjalankan iterasi dari 2 hingga 9. Loop dimulai dari 2 karena dua elemen pertama sudah ada di dalam list fibo, dan kita ingin menghasilkan 10 elemen dalam total.

# angka1 = fibo[i - 2] dan angka2 = fibo[i - 1]: Ini adalah dua variabel yang digunakan untuk menyimpan dua elemen terakhir dari list fibo. angka1 adalah elemen sebelumnya (indeks i - 2) dan angka2 adalah elemen saat ini (indeks i - 1).

# angkaSelanjutnya = angka1 + angka2: Ini adalah langkah untuk menghitung elemen selanjutnya dalam urutan Fibonacci. Elemen ini adalah hasil penjumlahan dari dua elemen sebelumnya, yaitu angka1 dan angka2.

# fibo.append(angkaSelanjutnya): Elemen angkaSelanjutnya ditambahkan ke akhir list fibo. Dengan demikian, list fibo terus berkembang dengan setiap iterasi, dan elemen-elemennya menjadi semakin besar sesuai dengan urutan Fibonacci.

# Setelah loop selesai berjalan, hasil akhir dari urutan Fibonacci yang telah dihasilkan akan dicetak ke layar dengan perintah print(fibo).