class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.values = []
    
    def enqueue(self, value, priority):
        node = Node(value, priority)
        valueList = []
        self.values.append(node)
        if(len(self.values)>1):
            self.bubbleUp()
        for nd in self.values:
            valueList.append(nd.value)
        print(valueList)
        return valueList

    def bubbleUp(self):
        idx = len(self.values)-1
        while(idx > 0):
            pIdx = (idx-1)//2
            childNode = self.values[idx]
            parentNode = self.values[pIdx]
            if(childNode.priority < parentNode.priority):
                self.values[pIdx] = childNode
                self.values[idx] = parentNode
                idx = pIdx
            else: break

pq = PriorityQueue()
pq.enqueue(5,5)
pq.enqueue(3,3)
pq.enqueue(4,4)
pq.enqueue(1,1)
pq.enqueue(2,2)
pq.enqueue(100,100)
pq.enqueue(0,0)