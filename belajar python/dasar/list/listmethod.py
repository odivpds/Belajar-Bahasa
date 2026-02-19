numbers = [1,2,3,4,5,6]
print(numbers)


#append digunakan untuk menambahkan list pada posisi paling akhir 
numbers.append(10)
print(numbers)


#insert digunakan untuk menambahkan list sesuai dengan index yang diinginkan
numbers.insert(5, 9) #(index yang ingin di masukan angka, angka yang akan mengisi index tersebut)
print(numbers)


#pop digunakan untuk menghapus list tetapi dengan acuan index
numbers.pop(5) #pop(index ke 5)
print(numbers)


#remove digunakan untuk menghapus list tetapi dengan acuan isi list tersebut
numbers.remove(1)#remove(list berisikan angka 1)
print(numbers)


#sort digunakan untuk mengurutkan list dari secara ascending
numbers.sort()
print(numbers)
