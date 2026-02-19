#menampilkan list pada path yang ada
def all_path(graph,start,end,path=[]):
    path=path+[start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths=[]
    for node in graph[start]:
        if not node in path:
            newpath = all_path(graph,node,end,path)
            for newpaths in newpath:
                paths.append(newpaths) 
    return paths

#untuk memnculkan path
def displayBlock(paths):
    for i in range(len(paths)):
        print('Path: ',i+1,"=", paths[i])

#mencari semua path/jalur
def find_AllEdge(graph):
    ListEdge = []
    for keys in graph.keys():
        if graph[keys]!=[]:
            for value in graph[keys]:
                temp = keys+'=>'+value
                ListEdge.append(temp)
    return ListEdge

def shortest_path(graph,start,end,path=[]):
    path = path + [start]
    if start == end:
        return path
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = shortest_path(graph,node,end,path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def find_ListShortestPath(AllPath,ShortestPath):
    ListShortest = []
    for path in AllPath:
        if len(path) == len(ShortestPath):
            ListShortest.append(path)
    return ListShortest

graphSembarang = {
    'A' : ['C','D'],
    'B' : ['C','E'],
    'C' : ['A','B','D','E'],
    'D' : ['C','E'],
    'E' : ['C','B'],
    'F' : []
}


ListAll_Path = all_path(graphSembarang,'A','E')
displayBlock(ListAll_Path)

print('\n') # <-- untuk memberi sekat baris

SemuaEdge = find_AllEdge(graphSembarang)
displayBlock(SemuaEdge)


ShortPath = shortest_path(graphSembarang,'A','E')
ListShortPath = find_ListShortestPath(ListAll_Path,ShortPath)
print('\nShortest Path dan Alternative Route')
displayBlock(ListShortPath)