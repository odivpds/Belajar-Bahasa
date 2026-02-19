# ini adalah Kelas untuk merepresentasikan simpul/graf
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.visited = False

    def add_neighbor(self, node):
        self.neighbors.append(node)
        node.neighbors.append(self)  # ini adalah elemen yang menunjukan Jika graf tidak berarah, baris ini dapat dihapus


# Untuk memanggil Fungsi DFS
def dfs(node):
    node.visited = True
    print(node.name, end=' ')

    for neighbor in node.neighbors:
        if not neighbor.visited:
            dfs(neighbor)


# Untuk membangun graf
nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')

nodeA.add_neighbor(nodeB)
nodeA.add_neighbor(nodeC)
nodeB.add_neighbor(nodeD)
nodeB.add_neighbor(nodeE)
nodeC.add_neighbor(nodeF)

# Untuk memulai DFS dari simpul A
print("Hasil DFS:")
dfs(nodeA)