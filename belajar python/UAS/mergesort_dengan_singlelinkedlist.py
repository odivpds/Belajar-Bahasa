# Definisikan kelas Node untuk merepresentasikan setiap elemen dalam linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Definisikan kelas LinkedList untuk merepresentasikan linked list itu sendiri
class LinkedList:
    def __init__(self):
        self.head = None

    # Metode untuk menambahkan elemen baru ke linked list
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    # Metode untuk melakukan Merge Sort pada linked list
    def merge_sort(self, head):
        if head is None or head.next is None:
            return head

        mid = self._get_middle(head)
        mid_next = mid.next

        mid.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(mid_next)

        sorted_list = self._merge(left, right)
        return sorted_list

    # Metode untuk mendapatkan titik tengah linked list
    def _get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # Metode untuk menggabungkan dua linked list terurut menjadi satu linked list terurut
    def _merge(self, left, right):
        dummy_node = Node(0)
        tail = dummy_node

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

        return dummy_node.next

    # Metode untuk mencetak isi linked list
    def display(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()


# Fungsi untuk menampilkan menu kepada pengguna
def display_menu():
    print("1. Tambahkan elemen")
    print("2. Urutkan menggunakan Merge Sort")
    print("3. Tampilkan elemen")
    print("4. Keluar")


# Membuat objek linked list
linked_list = LinkedList()

while True:
    display_menu()
    choice = input("Pilih menu: ")

    if choice == "1":
        data = int(input("Masukkan elemen: "))
        linked_list.append(data)
        print("Elemen telah ditambahkan.")
    elif choice == "2":
        if linked_list.head is None:
            print("Linked list kosong. Tidak dapat melakukan Merge Sort.")
        else:
            linked_list.head = linked_list.merge_sort(linked_list.head)
            print("Linked list telah diurutkan menggunakan Merge Sort:")
    elif choice == "3":
        print("Elemen dalam linked list:")
        linked_list.display()
    elif choice == "4":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")
