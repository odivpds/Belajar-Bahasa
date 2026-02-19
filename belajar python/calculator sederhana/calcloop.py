operasi = ""
while operasi != "exit":

    operasi = input("masukan operasi : ")    
    if operasi == "exit":
        print("terimakasih <3 ")
        break

    if operasi != "+" and operasi != "-" and operasi != "*" and operasi != "/":
        print("operasi salah")
        continue
    angka1 = int(input("masukan angka pertama : "))
    angka2 = int(input("masukan angka kedua : "))

    if operasi == "+":
        print(f"{angka1} + {angka2} = {angka1 + angka2}")   

    elif operasi == "-":
        print(f"{angka1} - {angka2} = {angka1 - angka2}") 

    elif operasi == "*":
        print(f"{angka1} x {angka2} = {angka1 * angka2}")  

    elif operasi == "/":
        print(f"{angka1} : {angka2} = {angka1 / angka2}")   