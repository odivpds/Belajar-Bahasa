def factorial (n):
    if (n == 1) :
        return 1
    else:
        return n * factorial (n-1)

q = int(input("masukan angka yang ingin di faktorialkan :"))

print(factorial(q))




