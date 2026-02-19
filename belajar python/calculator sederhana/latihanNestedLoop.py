objek = str(input("masukan objek : "))
finish = int(input("masukan finish : "))

for i in range(1,finish+1):
    for j in range(1, i+1):
        print(objek, end="")

    print("")
