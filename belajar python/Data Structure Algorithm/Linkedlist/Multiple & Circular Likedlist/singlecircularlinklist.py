#class node
class Node : 
    def __init__(self,data):
        self.data = data
        self.next = None

#class single circular linkedlist
class circularLinkedList:
    def __init__(self):
        self.head = None
    #menambahkan data
    def add_data(self,data):
        newnode = Node(data)
        temp = self.head
        newnode.next = self.head
        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = newnode
        else:
            newnode.next = newnode
        self.head = newnode
    def print(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print(str(temp.data)+' ->'+str(temp.next.data))
                temp = temp.next
                if(temp == self.head):
                    break

list = circularLinkedList()
list.add_data(1)
list.add_data(2)
list.add_data(3)
list.add_data(4)
print('isi list : ')
list.print()