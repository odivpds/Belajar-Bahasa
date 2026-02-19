class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None  # Atribut yang menunjukkan simpul pertama dalam linked list

    def append(self, data):
        """
        Menambahkan elemen baru ke linked list
        """
        new_node = Node(data)  # Membuat simpul baru dengan data yang diberikan

        if self.head is None:  # Jika linked list masih kosong
            self.head = new_node  # Menjadikan simpul baru sebagai simpul pertama
        else:
            curr_node = self.head  # Menunjuk ke simpul pertama
            while curr_node.next:  # Melakukan iterasi sampai mencapai simpul terakhir
                curr_node = curr_node.next  # Pindah ke simpul berikutnya
            curr_node.next = new_node  # Menambahkan simpul baru sebagai simpul berikutnya

    def merge_sort(self, head):
        """
        Mengurutkan linked list menggunakan Merge Sort
        """
        if head is None or head.next is None:  # Jika linked list kosong atau hanya memiliki satu elemen
            return head

        mid = self._get_middle(head)  # Mendapatkan titik tengah linked list
        mid_next = mid.next  # Menyimpan simpul berikutnya setelah titik tengah

        mid.next = None  # Memutuskan hubungan antara bagian kiri dan bagian kanan

        left = self.merge_sort(head)  # Mengurutkan bagian kiri secara rekursif
        right = self.merge_sort(mid_next)  # Mengurutkan bagian kanan secara rekursif

        sorted_list = self._merge(left, right)  # Menggabungkan kedua linked list terurut
        return sorted_list

    def _get_middle(self, head):
        """
        Mengembalikan titik tengah linked list
        """
        if head is None:  # Jika linked list kosong
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:  # Melakukan iterasi dengan pendekatan "fast-slow"
            slow = slow.next
            fast = fast.next.next

        return slow  # Mengembalikan simpul tengah

    def _merge(self, left, right):
        """
        Menggabungkan dua linked list terurut menjadi satu linked list terurut
        """
        dummy_node = Node(0)  # Membuat simpul palsu sebagai simpul awal
        tail = dummy_node  # Menyimpan simpul terakhir saat melakukan penggabungan

        while left and right:
            if left.data <= right.data:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        if left:
            tail.next = left
        if right:
            tail.next = right

        return dummy_node.next  # Mengembalikan simpul pertama dari linked list hasil penggabungan

    def display(self):
        """
        Menampilkan isi linked list
        """
        curr_node = self.head
        while curr_node:  # Melakukan iterasi sampai mencapai simpul terakhir
            print(curr_node.data, end=" ")  # Menampilkan data simpul
            curr_node = curr_node.next  # Pindah ke simpul berikutnya
        print()


def display_menu():
    print("1. Tambahkan elemen")
    print("2. Urutkan menggunakan Merge Sort")
    print("3. Tampilkan elemen")
    print("4. Keluar")


# Membuat linked list
linked_list = LinkedList()

while True:
    display_menu()
    choice = input("Pilih menu: ")

    if choice == "1":
        data = int(input("Masukkan elemen: "))
        linked_list.append(data)
        print("Elemen telah ditambahkan.")
    elif choice == "2":
        if linked_list.head is None:  # Jika linked list kosong
            print("Linked list kosong. Tidak dapat melakukan Merge Sort.")
        else:
            linked_list.head = linked_list.merge_sort(linked_list.head)  # Mengurutkan linked list menggunakan Merge Sort
            print("Linked list telah diurutkan menggunakan Merge Sort:")
    elif choice == "3":
        print("Elemen dalam linked list:")
        linked_list.display()  # Menampilkan elemen-elemen dalam linked list
    elif choice == "4":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")




        
