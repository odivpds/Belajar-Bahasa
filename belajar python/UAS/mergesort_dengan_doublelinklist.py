class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Atribut yang menunjukkan simpul pertama dalam linked list

    def append(self, data):
        new_node = Node(data)  # Membuat simpul baru dengan data yang diberikan
        if self.head is None:  # Jika linked list masih kosong
            self.head = new_node  # Menjadikan simpul baru sebagai simpul pertama
        else:
            current = self.head  # Menunjuk ke simpul pertama
            while current.next:  # Melakukan iterasi sampai mencapai simpul terakhir
                current = current.next  # Pindah ke simpul berikutnya
            current.next = new_node  # Menambahkan simpul baru sebagai simpul berikutnya
            new_node.prev = current  # Menyambungkan simpul baru ke simpul sebelumnya

    def merge_sort(self):
        if self.head is None or self.head.next is None:  # Jika linked list kosong atau hanya memiliki satu elemen
            return self.head  # Kembalikan linked list tanpa perubahan

        mid = self._get_middle_node()  # Mendapatkan titik tengah linked list
        next_to_mid = mid.next  # Menyimpan simpul berikutnya setelah titik tengah

        mid.next = None  # Memutuskan hubungan antara bagian kiri dan bagian kanan

        left = DoublyLinkedList()  # Membuat linked list kiri
        left.head = self.head  # Menyimpan simpul pertama pada linked list kiri

        right = DoublyLinkedList()  # Membuat linked list kanan
        right.head = next_to_mid  # Menyimpan simpul pertama pada linked list kanan

        left.merge_sort()  # Mengurutkan linked list kiri secara rekursif
        right.merge_sort()  # Mengurutkan linked list kanan secara rekursif

        self.head = self._merge(left.head, right.head)  # Menggabungkan kedua linked list terurut

    def _merge(self, left, right):
        result = None

        if left is None:  # Jika linked list kiri sudah habis
            return right
        if right is None:  # Jika linked list kanan sudah habis
            return left

        if left.data <= right.data:  # Membandingkan elemen pertama dari kedua linked list
            result = left
            result.next = self._merge(left.next, right)  # Memanggil fungsi merge_sort() secara rekursif
            result.next.prev = result
        else:
            result = right
            result.next = self._merge(left, right.next)  # Memanggil fungsi merge_sort() secara rekursif
            result.next.prev = result

        return result

    def _get_middle_node(self):
        if self.head is None:  # Jika linked list kosong
            return self.head

        slow = self.head
        fast = self.head

        while fast.next and fast.next.next:  # Melakukan iterasi dengan pendekatan "fast-slow"
            slow = slow.next  # Berpindah satu simpul per iterasi
            fast = fast.next.next  # Berpindah dua simpul per iterasi

        return slow  # Mengembalikan simpul tengah

    def display(self):
        current = self.head
        while current:  # Melakukan iterasi sampai mencapai simpul terakhir
            print(current.data, end=" ")  # Menampilkan data simpul
            current = current.next  # Pindah ke simpul berikutnya
        print()


def display_menu():
    print("=== MENU ===")
    print("1. Tambahkan elemen")
    print("2. Tampilkan elemen")
    print("3. Urutkan dengan Merge Sort")
    print("4. Keluar")


# Contoh penggunaan
dll = DoublyLinkedList()

while True:
    display_menu()
    choice = input("Pilih menu (1/2/3/4): ")

    if choice == "1":
        data = int(input("Masukkan elemen: "))
        dll.append(data)
        print("Elemen ditambahkan.")

    elif choice == "2":
        print("Elemen dalam linked list:")
        dll.display()

    elif choice == "3":
        print("Sebelum sorting:")
        dll.display()

        dll.merge_sort()

        print("Setelah sorting:")
        dll.display()

    elif choice == "4":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

    print()
