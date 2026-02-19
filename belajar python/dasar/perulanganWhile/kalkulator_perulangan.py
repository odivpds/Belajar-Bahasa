perintah = ""
while perintah != "exit":

    perintah = input("pilih operasi: ")
    if perintah == "exit":
        break
    if perintah != "+" and perintah != "-" and perintah != "*" and perintah != "/":
        print("perintah tidak dikenali :(")
        continue
    
    num1 = int(input("masukan angka: "))
    num2 = int(input("masukan angka: "))

    if  perintah == "+":
        print(num1 + num2)

    elif perintah == "-":
        print(num1 - num2)

    elif perintah == "*":
        print(num1 * num2)

    elif perintah == "/":
        print(num1 / num2)

    elif perintah == "exit":
        break
print("terimakasi sudah menggunakan kalkulator ini :)")