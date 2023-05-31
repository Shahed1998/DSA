class Graph:
    def __init__(self):
        self.adjacencyList = {}

    def addVertex(self, vertex):
        # prevents duplicates from over writing
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex] = []


g = Graph()
g.addVertex("Tokyo")
g.addVertex("Dhaka")
# g.adjacencyList["Tokyo"].append("Dhaka")
print(g.adjacencyList)
