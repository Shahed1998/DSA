class CircularQueue:
    def __init__(self, capacity):
        self.arr = [None] * capacity # Defined Queue size
        self.front = 0
        self.rear = -1
        self.capacity = capacity
        self.size = 0

    def push(self, val):

        if self.size >= self.capacity:  return print("Queue is full")

        self.rear = (self.rear + 1) % self.capacity
        self.arr[self.rear] = val
        self.size += 1

    def pop(self):
        if self.size <= 0: return print("Queue is empty")

        tmp = self.arr[self.front]
        self.arr[self.front] = None

        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        return tmp
    
    def first(self): return self.arr[self.front]

# --------------------------------------------------------------------------------------------------
# Test cases 
# --------------------------------------------------------------------------------------------------

cq = CircularQueue(5)
cq.push(1)
cq.push(2)
cq.push(3)
cq.push(4)
cq.push(5)
cq.pop()
cq.push(6)
cq.pop()
cq.push(7)
cq.pop()
cq.push(8)
cq.pop()
cq.push(9)
cq.pop()
cq.push(10)
cq.push(11)
cq.pop()
cq.pop()
cq.pop()
cq.pop()
cq.pop()
cq.pop()
# print(cq.arr)
# print(cq.first())
