#menggunkanan perulangan biasa (output = menampilkan angka sesuai perintah baris dan kolom yang dituju)
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], # = array ke 0
                [[7, 8, 9], [10, 11, 12]], # = array ke 1
                [[7, 1, 8], [6,15, 13]]]) # = array ke 2
print(arr [0,1,0]) # = print(arr [array ke n, kolom ke n, baris ke n])