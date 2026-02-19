class Node:
    def _init_(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyCircularLinkedList:
    def _init_(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = self.head
            self.head.prev = new_node

    def print_list(self):
        if not self.head:
            print("List is empty")
        else:
            current = self.head
            while True:
                print(current.data, end=" ")
                current = current.next
                if current == self.head:
                    break

# contoh penggunaan
dllist = DoublyCircularLinkedList()
dllist.insert_at_end(1)
dllist.insert_at_end(2)
dllist.insert_at_end(3)
dllist.print_list() # output: 1 2 3