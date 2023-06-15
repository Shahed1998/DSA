class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None


# Doubly Linked List
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = self.head
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = self.tail.next
        self.length += 1

    def get(self, value):
        current = self.head
        for i in range(self.length):
            if current.value == value:
                return current
            current = current.next
        return None

    def remove(self, vertex):
        n = self.get(vertex)
        if n == None:
            return False
        prev = n.prev
        next = n.next

        # Test case for only one element in the list
        if prev == None and next == None:
            self.head = None
        # Test case for removing only the first element
        elif (prev == None) and (not next == None):
            self.head = self.head.next
            self.head.prev = None
        # Test case for removing the last element
        elif (not prev == None) and (next == None):
            self.tail = self.tail.prev
            self.tail.next = None
        # Test case for removing from the middle
        else:
            prev.next = next
            next.prev = prev

        n = None
        self.length -= 1
        return True


class Graph:
    def __init__(self):
        self.adjacencyList = {}

    def addVertex(self, vertex):
        # prevents duplicates from over writing
        if vertex not in self.adjacencyList:
            dll = DLL()
            self.adjacencyList[vertex] = dll

    def checkValidVertex(self, vertex1=None, vertex2=None):
        # checks for invalid vertex in adjacencyList
        if (not vertex1 == None) and (vertex1 not in self.adjacencyList):
            raise Exception(f"Invalid vertex {vertex1}")
        elif (not vertex2 == None) and (vertex2 not in self.adjacencyList):
            raise Exception(f"Invalid vertex {vertex2}")

    def addEdge(self, vertex1, vertex2):
        self.checkValidVertex(vertex1, vertex2)
        self.adjacencyList[vertex1].push(vertex2)
        self.adjacencyList[vertex2].push(vertex1)

    def removeEdge(self, vertex1, vertex2):
        self.checkValidVertex(vertex1)
        rm1 = self.adjacencyList[vertex1].remove(vertex2)
        rm2 = self.adjacencyList[vertex2].remove(vertex1)
        if not (rm1 and rm2):
            return "Vertices are not connected"
        return "Connection severed"

    # Task: Remove vertex
    def removeVertex(self, vertex):
        self.checkValidVertex(vertex)
        del self.adjacencyList[vertex]  # Removing vertex from the dictionary
        for key, value in self.adjacencyList.items():
            value.remove(vertex)
        return self.adjacencyList


# ------------------------------------------
# Test cases
# ------------------------------------------

# g = Graph()

# g.addVertex("Tokyo")
# g.addVertex("Dhaka")
# g.addVertex("Chittagong")
# g.addVertex("Newfoundland")

# g.addEdge("Tokyo", "Dhaka")
# g.addEdge("Tokyo", "Newfoundland")
# g.addEdge("Dhaka", "Newfoundland")
# g.addEdge("Dhaka", "Chittagong")

# print(g.removeVertex("Chittagong")['Dhaka'].head.next.next)

# print(g.removeEdge("Tokyo", "Newfoundland"))
# print(g.adjacencyList["Newfoundland"].head.value)

# print(g.adjacencyList['Dhaka'].length)
# print(g.adjacencyList['Newfoundland'].length)
# print(g.adjacencyList['Chittagong'].length)

# ------------------------------------------
# Doubly Linked List Test cases
# ------------------------------------------
# dll = DLL()
# dll.push(1)
# dll.push(2)
# dll.push(3)
# dll.push(4)

# # Head to Tail
# print(dll.head.value)
# print(dll.head.next.value)
# print(dll.head.next.next.value)
# print(dll.head.next.next.next.value)
# print(dll.head.next.next.next.next)

# # Tail to Head
# print(dll.tail.value)
# print(dll.tail.prev.value)
# print(dll.tail.prev.prev.value)
# print(dll.tail.prev.prev.prev.value)
# print(dll.tail.prev.prev.prev.prev)
