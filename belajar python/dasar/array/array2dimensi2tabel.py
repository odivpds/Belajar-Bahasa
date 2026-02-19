#2table
import numpy as np
arr = np.array([[[10,9,8,7,6], [6,5,4,3,2]],
                [[1,2,3,4,5],[6,7,8,9,10]]])
print(arr[0,1,2]) 
#print(arr[array ke n, kolom ke n, baris ke n])

#merubah data pada array diatas
arr [0,1,2] = 15
print(arr[0,1,2]) # pemanggilan menggunakan koma ini hanya untuk tuple

# jika object array maka pemanggilan menggunakan arr[0][1][2]