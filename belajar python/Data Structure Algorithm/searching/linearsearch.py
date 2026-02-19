def search(arr, x):
    for i in range(len(arr)):
        if arr [i] == x:
            return i
    return -1

# mencari dengan cara rekursif
def recsearch(arr,x,current_index):
    if current_index==-1:
        return -1
    if arr[current_index] == x:
        return current_index
    return recsearch(arr,x,current_index-1)

arr=[35,23,65,12,88,43,2,79]
x=43

print("Angka",x,"berada pada index ke",(search(arr,x)))
# hasil= search(arr,x)
# print(arr[hasil])

# menampilkan cara rekursif
print(recsearch(arr,x,len(arr)-1))