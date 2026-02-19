import numpy as np # ini  digunakan apabila ingin memasukan array ke dalam tuple(), jika anda tidak ingin memakai tuple() maka tidak perlu import numpy, contoh ada di akses list

#semua output merupakan array

#membuat vector
a = np.array ([1,2,3,4,5])
b = np.array ([1.5, 2, 3.5, 4, 5.5])

#membuat vector dengan range
c= np.arange (1,10,2) # (angka dimualainya, batas angka, gap atau sekat antar angka)

#membuat linspace
d= np.linspace (0,10,5) #(angka start, angka end, angka yang digunakan sebagai pembagi)
# output = [0 2.5 5 7.5 10] karena angka yang digunakan sebagai pembagi adalah 5, maka index yang terdapat diantara 0-10 akan terbagi menjadi 5, yang tadinya terdapat 10 angka atau 11 index menjadi 5 index saja

#membuat listrange
e= list(range(1, 11)); # (angka start, angka end-1)

#array multidimensi/matriks
f= np.array ([ (1,2,3),(4,5,6)])

#matriks dengan niai nol
g= np.zeros ((5,5))

#matriks dengan nilai satu
h= np.ones ((5,5))

print(g)