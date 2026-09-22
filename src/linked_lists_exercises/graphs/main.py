class DirectedGraph: 
    def __init__(self):
        self.adjlist = {}




    def add_edge(self, source, sink, weight):
        if source not in self.adjlist:
            self.adjlist[source] = {}
        self.adjlist[source][sink] = weight


class UndirectedGraphAndUnPonderedGraph:
    def __init__(self):
        self.adjlist = {}

    def add_edge(self, source, sink, weight):
        if source not in self.adjlist:
            self.adjlist[source] = {}
        if sink not in self.adjlist:
            self.adjlist[sink] = {}
        self.adjlist[source][sink] = weight
        self.adjlist[sink][source] = weight




# g = DirectedGraph()
# g.add_edge(0, 1, 8)
# g.add_edge(1, 0, 5)
# g.add_edge(1, 5, 3)
# g.add_edge(2, 0, 7)
# g.add_edge(2, 4, 9)
# g.add_edge(3, 1, 5)
# g.add_edge(3, 4, 7)
# g.add_edge(4, 2, 6)


# print(g.adjlist)




p = UndirectedGraphAndUnPonderedGraph()
p.add_edge(0, 1, 8)
p.add_edge(1, 0, 5)
p.add_edge(1, 5, 3)
p.add_edge(2, 4, 9)
print(p.adjlist)