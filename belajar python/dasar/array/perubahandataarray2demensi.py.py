#perubahan data untuk array 2 demensi
import numpy as np
arr = np.array ([[10,9,8,7,6], # = array ke 0
                [6,5,4,3,2]])  # = array ke 1
print(arr[1,3],['array sebelumnya'])
#print(arr[array ke n, baris ke n])

arr [1] [3] = 9
print(arr[1,3],['array setelah diubah'])
