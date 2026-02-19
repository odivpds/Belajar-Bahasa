perintah =""
while perintah != "Done":

    perintah = input("masukan operasi: ")
    if perintah == "done":
        print("Thanks")
        break

    if perintah != "+" and perintah != "-" and perintah != "*" and perintah != "/":
        print("maaf perintah tidak dikenali")
        continue
    
    a = int(input("masukan angka pertama: "))
    b = int(input("masukan angka kedua: ")) 
    
     
    if perintah == "+":
        print(a + b)
    
    elif perintah == "-":
        print(a - b)
    
    elif perintah == "*":
        print(a * b)
    
    elif perintah == "/":
        print(a / b)
     