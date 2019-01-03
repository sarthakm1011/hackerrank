import queue
from collections import defaultdict

class Graph():
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = defaultdict(lambda:[])

    def connect(self,x,y):
        #print(x) # Starting node index
        #print(y) # ending node index
        self.edges[x].append(y)
        self.edges[y].append(x)
        
    
    def find_all_distances(self, root):    
        distances = [-1 for i in range(self.nodes)]
        unvisited = set([i for i in range(self.nodes)])
        q = queue.Queue()

        distances[root] = 0 # distance with itself
        unvisited.remove(root)
        q.put(root)

        while not q.empty():
            node = q.get()
            children = self.edges[node]
            height = distances[node]
            for child in children:
                if child in unvisited:
                    distances[child] = height + 6
                    unvisited.remove(child)
                    q.put(child) # put all visting childs in q

        distances.pop(root)
        
        #print(distances)
        print(" ".join(map(str,distances)))



t = int(input()) # number of queries
for i in range(t):
    n,m = [int(value) for value in input().split()]
    #print(n) # number of nodes in a query
    #print(m) # number of edges in a query
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1, y-1) 
    
    s = int(input())
    graph.find_all_distances(s-1)
    
