def tampilkanAngka (batas, i = 10) :
    print (f'perulangan ke {i}')
    if (i > batas) :
        tampilkanAngka (batas, i - 1)
    
tampilkanAngka (0,10)