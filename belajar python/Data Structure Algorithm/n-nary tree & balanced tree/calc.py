operasi = ""

while operasi != "exit":
    print()
    operasi = input("masukan operasi: ")
    if operasi =="exit":
        print("terimakasi :)")
        break
    if operasi != "+" and operasi != "-" and operasi != "*" and operasi != "/":
        print("operasi tidak dapat ditemukan :) ")
        continue
    angka1 =int(input("masukan angka1: "))
    angka2 =int(input("masukan angka2: "))
    
    
    if operasi =="+":
        print(angka1+angka2 )
    elif operasi =="-":
        print(angka1-angka2 )
    elif operasi =="*":
        print(angka1*angka2 )
    elif operasi =="/":
        print(angka1/angka2 )    