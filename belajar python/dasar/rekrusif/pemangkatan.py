def multiply (x,n) :
    if (n == 0) :
        return 1
    else:
        return x* multiply (x, n-1)
    
q = (multiply)(int(input("masukan bilangan: ")),(int(input("masukan pangkat: "))))

print (f"hasil pemangkatan bilangan diatas adalah {q}")

