class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [None] * k
        self.first = 0
        self.last = -1
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:

        if self.size >= self.capacity: return False

        self.last = (self.last + 1) % self.capacity
        self.arr[self.last] = value

        self.size += 1

        return True

    def deQueue(self) -> bool:

        if self.size <= 0: return False

        self.arr[self.first] = None

        self.first = (self.first + 1) % self.capacity

        self.size -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1 
        return self.arr[self.first]

    def Rear(self) -> int:
        if self.isEmpty(): return -1 
        return self.arr[self.last]

    def isFull(self) -> bool: return self.size >= self.capacity 
 
    def isEmpty(self) -> bool: return self.size <= 0
        
# -------------------------------------------------------------------------------------
# Test Case 01 
# -------------------------------------------------------------------------------------
# obj = MyCircularQueue(3)
# print(obj.enQueue(7))
# print(obj.deQueue())
# print(obj.Front())
# print(obj.deQueue())
# print(obj.Front())
# print(obj.Rear())
# print(obj.enQueue(0))
# print(obj.isFull())
# print(obj.deQueue())
# print(obj.Rear())
# print(obj.enQueue(3))

# -------------------------------------------------------------------------------------
# Test Case 02
# -------------------------------------------------------------------------------------
# obj = MyCircularQueue(3) #null
# print(obj.enQueue(1)) #true
# print(obj.enQueue(2)) #true
# print(obj.enQueue(3)) #true
# print(obj.enQueue(4)) #false
# print(obj.Rear()) #3
# print(obj.isFull()) #true
# print(obj.deQueue()) #true
# print(obj.enQueue(4)) #true
# print(obj.Rear()) #4

