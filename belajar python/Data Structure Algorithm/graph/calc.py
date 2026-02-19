operasi = ""
while operasi != "exit":
    print()
    operasi =input("Masukan operasi: ")
    if operasi == "exit":
        print("terimakasi :)")
        break
    
    if operasi != "+" and operasi != "-" and operasi != "*" and operasi != "/":
        print("operasi unknown")
        continue
    
    a = int(input("Masukan Angka Pertama: "))
    b = int(input("Masukan Angka Kedua: "))
               
    if operasi =="+":
        print(a + b)
    
    elif operasi == "-":
        print(a - b)
    
    elif operasi == "*":
        print(a * b)
        
    elif operasi == "/":
        print(a / b)