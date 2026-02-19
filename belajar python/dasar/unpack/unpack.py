numbers = [1, 2, 3]

# X = (0)
# Y = (1)
# Z = (2)


# memanggil semua value dari array
x, y, z = numbers
print(numbers ) # ini akan memunculkan semua value dari numbers

# untuk memanggil salah satu array
x, _, _ = numbers
print(x) # maka ini akan memunculkan value dari index ke 0 yaitu 1

# memanggil salah satu array dan mebungkus array lain ke dalam variable a
x,*a = numbers
print(x) # 1
print(a) # [2,3]