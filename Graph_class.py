
class Vertex:
    def __init__(self,value):
        self.value = value
        self.edges = {}

    def add_edge(self,vertex,weight=0):
        self.edges.update({vertex:weight})


class Graph:
    def __init__(self,):
        self.vertices ={}

    def add_vertex(self,vertex):
        self.vertices[vertex.value]=vertex

    def add_edge(self,from_vertex,to_vertex):
        self.vertices[from_vertex].add_edge(self.vertices[to_vertex])
        self.vertices[to_vertex].add_edge(self.vertices[from_vertex])

    def dfs(self,root_vertex,visited = []):
        self.visited = visited
        if self.vertices[root_vertex].value not in self.visited:
            self.visited.append(self.vertices[root_vertex].value)
            print(self.vertices[root_vertex].value,end=' ')
            for vertex in self.vertices[root_vertex].edges:
                self.dfs(vertex.value,self.visited)

    def bfs(self,root):
        self.visited = []
        self.next_tovisit=[root]
        while len(self.next_tovisit)!=0:
            current = self.next_tovisit.pop(0)
            print(current,end =' ')
            self.visited.append(current)
            for child in self.vertices[current].edges:
                if child.value not in self.visited and child.value not in self.next_tovisit :
                    self.next_tovisit.append(child.value)




if __name__ == '__main__':
    G = Graph()
    G.add_vertex(Vertex('Pritom'))
    G.add_vertex(Vertex('Monika'))
    G.add_vertex(Vertex('Sanjoy'))
    G.add_vertex(Vertex('Juna'))
    G.add_vertex(Vertex('Pritty'))
    G.add_vertex(Vertex('X'))
    G.add_vertex(Vertex('Y'))
    G.add_edge('Pritom','Juna')
    G.add_edge('Pritom','Monika')
    G.add_edge('Pritom','Sanjoy')
    G.add_edge('Sanjoy','Monika')
    G.add_edge('Sanjoy','Pritty')
    G.add_edge('Monika','Pritty')
    G.add_edge('X','Pritty')
    G.add_edge('Sanjoy','Y')
    print('DFS result:')
    G.dfs('Pritom')
    print('\nBFS result:')
    G.bfs('Pritom')



    





