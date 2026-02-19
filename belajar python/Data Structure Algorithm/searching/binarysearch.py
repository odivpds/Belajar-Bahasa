def search(arr,x):
    low = 0
    mid = 0
    high = len(arr)-1
    while low <= high:
        mid = (high + low) // 2
        if(arr[mid]< x):
            low = mid + 1
        elif(arr[mid]>x):
            high = mid -1
        else:
            return mid
    return -1

#cara rekursif
def recsearch(arr,low,high,x):
    if high >= low:
        mid = (low+high)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return recsearch(arr,low,high-1,x)
        else:
            return recsearch(arr,mid+1,high,x)
    else:
        return -1


arr = [20,21,22,23,24,25,26,27,28]
x = int(input("Masukan angka yang ada di dalam array: "))
if (search(arr,x)):
    print("angka",x,"berada pada index ke",(search(arr,x)))
else:
    print("angka tidak ditemukan")
    
# menampilkan dengan cara biasa
result = search(arr,x)
print("angka",x,"berada pada index ke",(result))

# menampilkan angka dengan cara rekursif
print("angka",x,"berada pada index ke",(recsearch(arr,0,len(arr)-1,x)))
