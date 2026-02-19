import os 
os.system("cls")

print("PROGRAM TAMPIL ANGKA")
a = int(input("Masukan Start : "))
b = int(input("Masukan Finish: "))
 
if a < b: 
    for i in range (a,b+1): # penggunaan "plus" pada parameter b untuk memunculkan angka Finish karena index dalam pemrograman dimulai dari angka 0
        print(i)
else:
    for i in reversed (range(b,a+1)):
        print(i)
