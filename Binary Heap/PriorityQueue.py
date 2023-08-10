class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.values = []

    def enqueue(self, value, priority):
        node = Node(value, priority)
        self.values.append(node)
        if (len(self.values) > 1):
            self.bubbleUp()

    def bubbleUp(self):
        idx = len(self.values)-1
        while (idx > 0):
            pIdx = (idx-1)//2
            childNode = self.values[idx]
            parentNode = self.values[pIdx]
            if (childNode.priority < parentNode.priority):
                self.values[pIdx] = childNode
                self.values[idx] = parentNode
                idx = pIdx
            else:
                break

    def dequeue(self):
        if len(self.values) == 0:
            return None
        if len(self.values) == 1:
            return self.values.pop(0).value
        return self.bubbleDown()

    def bubbleDown(self):
        idx = len(self.values)-1  # last index
        ret = self.values[0].value
        self.values[0] = self.values[idx]
        self.values.pop()
        idx = 0
        leftChildPriority = rightChildPriority = 0

        while True:
            leftChild = 2*idx+1
            rightChild = 2*idx+2
            currentNode = self.values[idx]
            currentNodePriority = self.values[idx].priority
            swap = 0

            if leftChild < len(self.values):
                leftChildPriority = self.values[leftChild].priority
                if currentNodePriority > leftChildPriority:
                    swap = leftChild

            if rightChild < len(self.values):
                rightChildPriority = self.values[rightChild].priority
                if leftChildPriority > rightChildPriority:
                    swap = rightChild

            if swap == 0:
                break

            self.values[idx] = self.values[swap]
            self.values[swap] = currentNode
            idx = swap

        return ret

    def printQueue(self):
        valueList = []
        for nd in self.values:
            valueList.append(nd.value)
        print(valueList)


# Test cases
# pq = PriorityQueue()
# pq.enqueue(5, 5)
# pq.enqueue(3, 3)
# pq.enqueue(4, 4)
# pq.enqueue(1, 1)
# pq.enqueue(2, 2)
# pq.enqueue(100, 100)
# pq.enqueue(0, 0)
# pq.dequeue()
# # pq.printQueue()
# pq.dequeue()
# # pq.printQueue()
# pq.dequeue()
# # pq.printQueue()
# pq.dequeue()
# pq.printQueue()
# # pq.dequeue()
# # pq.printQueue()
# # pq.dequeue()
# # pq.printQueue()
# # pq.dequeue()
# # pq.printQueue()
# # pq.dequeue()
# # pq.printQueue()
