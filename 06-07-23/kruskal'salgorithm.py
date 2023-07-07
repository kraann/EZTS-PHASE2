def krushals(graph):
    edge_list=[]
    for source in graph:
        for edge in graph[source]:
            weight, dest=edge
            edge_list.append((weight, source, dest))
        edge_list.sort()

        parents={}
        for vertex in graph:
            parents[vertex]=vertex
        mst=[]
        
graph={
    'A':[(1,'B'),(3,'E')],
    'B':[(1,'A'),(2,'E'),(1,'D'),(4,'C')],
    'C':[(4,'B'),(1,'D')],
    'D':[(1,'B'),(1,'C'),(2,'E')],
    'E':[(3,'A'),(2,'B'),(2,'D')]
    }

mst=krushals(graph)
print(mst)

