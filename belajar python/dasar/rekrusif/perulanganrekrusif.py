def tampilkanAngka (batas, i = 1) :
    print (f'perulangan ke {i}')
    if (i < batas) :
        tampilkanAngka (batas, i + 1)
    
tampilkanAngka (10,0)