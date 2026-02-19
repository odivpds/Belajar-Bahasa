# 1. Segitiga sama kaki
tinggi = 10
for data in range(1,tinggi+1):
    for i in range(tinggi-data):
        print(" ",end="")

    for j in range(2*data-1):
        print("*",end="")

    print()        
