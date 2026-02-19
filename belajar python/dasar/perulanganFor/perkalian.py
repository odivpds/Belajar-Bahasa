import os 
os.system("cls")

print("program bilangan bulat i hingga x")
k =int(input('masukan perkalian :'))
i = int(input("masukan angka :"))
x = int(input("masukan angka :"))

for i in range (k,x+1):
    print(k,"X",i,"=",i*k)