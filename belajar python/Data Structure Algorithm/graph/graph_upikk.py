#menampilkan list pad yang ada
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

#untuk mendisplayy path
def displayBlock(paths):
    for i in range(len(paths)):
        print('Path : ',i+1," = ",paths[i])

#mencari semua path/jalur
def find_AllEdge(graph):
    ListEdge = []
    for keys in graph.keys():
        if graph[keys] != []:
            for value in graph[keys]:
                temp = keys+'=>'+value
                ListEdge.append(temp)
        return ListEdge


graphSembarang = {
    'A' : ['C','D'],
    'B' : ['C', 'E'],
    'C' : ['A', 'B', 'D', 'E'],
    'D' : ['C', 'E'],
    'E' : ['C', 'B'],
    'F' : []
}

ListAll_Path = all_path(graphSembarang, 'A', 'E')
displayBlock(ListAll_Path)

SemuaEdge = find_AllEdge(graphSembarang)
displayBlock(SemuaEdge)