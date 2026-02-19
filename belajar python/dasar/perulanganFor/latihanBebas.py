# objek = str(input("masukan objek : "))

# for i in range(1,10+1):
#     for j in range(1,i+1):
#         print(objek,end="")
#     print()    

# for i in reversed(range(1,10+1)):
#     for j in reversed(range(1,i+1)):
#         print(objek,end="")
#     print()       


nilaiSiswa = int(input("masukan nilai siswa : "))
if nilaiSiswa > 100:
    print("UNDIFINED");

if nilaiSiswa >= 90 and nilaiSiswa <= 100:
    print('Nilaimu : A');
elif nilaiSiswa >= 80 and nilaiSiswa < 90:
    print('Nilaimu : B');
elif nilaiSiswa >= 70 and nilaiSiswa < 80:
    print('Nilaimu : C');
elif nilaiSiswa >= 60 and nilaiSiswa < 70:
    print('Nilaimu : D');
elif nilaiSiswa >= 50 and nilaiSiswa < 60:
    print('Nilaimu : E');
else :
    print('Belajar lebih giat lagi');


