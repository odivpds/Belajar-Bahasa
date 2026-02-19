print("Pilihlah Ucapan selamat :")
print("pagi")
print("malam")

dayTime = str(input("Input dayTime : "))

if dayTime != "pagi" and dayTime != "malam":
    print("salah")

elif dayTime == "pagi":
    print("selamat pagi div")
    print("selamat beraktivitas yaaa")

elif dayTime == "malam":
    print("selamat malam div")
    print("selamat tidur yaa")

else:
    print("gatau apaa div")
