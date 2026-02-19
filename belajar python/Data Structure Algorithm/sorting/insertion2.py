def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i].lower()
        j = i-1
        while j >= 0 and key.lower() < arr[j]:#<--lower untuk menganggap variabel capitalia tidak ada 
            arr[j+1] = arr[j]
            j-=1
            arr[j+1] = key
# arr = [6,1,3,7,2]
arr=[]
loop = int(input("Berapa Nilai: "))
for i in range(1,loop):
    inp = str(input("Masukan Karakter ke -" +str(i)))
    arr.append(inp)
insertionSort(arr)
print(arr)
