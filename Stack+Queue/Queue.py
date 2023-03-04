class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None 
        self.size = 0
    
    def enqueue(self, val):
        node = Node(val)
        if(self.size == 0):
            self.first = node
            self.last = self.first
        else:
            self.last.next = node
            self.last = node
        self.size += 1
        return self.size
    
    def dequeue(self):
        if self.size == 0: return None        
        current = self.first
        if self.size == 1:
            self.first = None
            self.last = None
        else:
            self.first = current.next
            current.next = None
        self.size -= 1
        return current



        
# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# # print(queue.size)
# print(queue.first.value, queue.last.value, queue.size)
# print(queue.dequeue().value)
# print(queue.dequeue().value)
# print(queue.dequeue().value)
# print(queue.dequeue().value)
# print(queue.first, queue.last, queue.size)