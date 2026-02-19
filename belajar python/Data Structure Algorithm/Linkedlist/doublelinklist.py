#class node
class Node(object) :
    #inisialisasi node
    def __init__(self, data, next,prev):
        self.data = data
        self.next = next
        self.prev = prev

class Doublelist(object) :
    head = None
    tail = None
    
    #menambahkan data
    def menuTambah(self) :
        inp = int(input('masukan data :'))
        new_node = Node(inp, None, None)
        if self.head is None:
            #menunjukan head dan tail ke node baru
            self.head = self.tail = new_node
        #ketika list head dan tail ke node baru    
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    #menghapus node
    def menuHapus(self):
        inp = int(input('masukan data yang ingin dihapus :'))
        #point untuk menunjukan node pertama
        current_node = self.head
        #lakukan perulangan sebanyak node
        while current_node is not None:
            #memeriksa apakah data tersebut yang ingin dihapus
            if current_node.data == inp:
                #cek apakah data tersebut di elemen node terakhir
                if current_node.next is None :
                    current_node.prev = None
                #jika node yang dicari bukan di elemen node pertama
                elif current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                #jika node berada di elemen pertama
                else:
                    self.head = current_node.next #memindahkan head ke elemen berikutnya
                    current_node.next.prev = None #menunjuk head prev menjadi none

            #memindahkan pointer menuju ke node berikutnya
            current_node = current_node.next
    
    #menu melihat isi list
    def menuTampil(self) :
        print('list data : ')
        #membuat pointer untuk menunjuk ke node pertama
        current_node = self.head
        #perulangan menampilkan data beserta data sebelum dan setelahnya
        while current_node is not None:
            print(current_node.prev.data) if hasattr(current_node.prev,"data") else None
            print(current_node.data)
            print(current_node.next.data) if hasattr(current_node.next,"data") else None
            #menunjuk ke node berikutnya
            current_node = current_node.next
            
    def menuUmum(self):
        pilih = "y"
        while ((pilih == "y") or (pilih == "Y")):
            print('pilih menu :')
            print('1. tambah data')
            print('2. hapus data')
            print('3. tampil data')
            pilihan = str(input('masukan pilihan : '))
            if(pilihan == "1"):
                self.menuTambah()
            elif(pilihan == "2"):
                self.menuHapus()
            elif(pilihan == "3"):
                self.menuTampil()
            else:
                pilih  = "n"
            
if __name__ == "__main__":
    dl = Doublelist()
    dl.menuUmum()
    