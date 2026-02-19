#cara menggunakan perulangan (output = bilangan akan berjejer kebawah)
import numpy as np
arr = np.array([[10,9,8,7,6],
                [6,5,4,3,2]])
for x in arr:
    for y in x:
       print(y) 

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# menggunakan cara biasa (output = bilangan akan muncul sesuai perintah baris dan kolom)
import numpy as np
arr = np.array([[1,2,3,4,5], #array ke 0
                [6,7,8,9,10]])#array ke 1
print(arr[0,2])
#print(arr[array ke n, baris ke n])
