def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
            arr[j+1] = key
# arr = [6,1,3,7,2]
arr=[]
loop = int(input("Berapa Nilai: "))
for i in range(1,loop):
    inp = int(input("Masukan Nilai ke -" +str(i)))
    arr.append(inp)
insertionSort(arr)
print(arr)
print