import os 
os.system("cls")
a=[]
b=[]
c=[]
for i in range(4):
    a_ = int(input("masukan angka ke :"))
    a.append(a_)

print()
print("Angka ke 1 adalah: ", a[0])
print("Angka ke 2 adalah: ", a[1])
print("Angka ke 3 adalah: ", a[2])
print("Angka ke 4 adalah: ", a[3])

for i in range(4):
    print("a[",i,"] ; ",a[i])
