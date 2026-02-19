coba_tebak = 0
angka_rahasia = 4
kesempatan = 3

while coba_tebak < kesempatan:
#setelah memasukan while harus memasukan variable baru untuk dilakukan perulangan pada variable tsb.
    angka_tebakan = int(input("masukan angka (1-9): ")) 
    if angka_tebakan > 9 :
        print("UNDIFINED")
        print("coba lagi *angka rahasia berada di angka 1-9")
        continue
    coba_tebak +=1

    if angka_tebakan != angka_rahasia and coba_tebak >= kesempatan : 
        print("kesempatan habis hahahahaha anda kalah ")
    
    elif angka_tebakan == angka_rahasia:
        print("selamat kamu menang")
        break