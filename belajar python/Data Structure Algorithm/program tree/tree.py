class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
            
tree = Node(2) #root
tree.left = Node(3) #child root kiri
tree.right = Node(4) #child root kanan
tree.left.left = Node(5) #child 3 kiri
tree.left.right = Node(6) #child 3 kanan
tree.right.left = Node(7) #child 4 kiri
tree.right.right = Node(8) #child 4 kanan
tree.PrintTree()