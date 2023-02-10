class Node:

    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None

class DLL:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1
        return self

    def pop(self):
        if self.head == None:
            return None
        elif self.head.next == None and self.tail.prev == None:
            self.head = None
            self.tail = None
        else:
            oldTail = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            oldTail.prev = None
        self.length -= 1
        return self
          
    def shift(self):
        if self.length == 0: return None
        elif self.length == 1:
            self.length -= 1
            self.head = None
            self.tail = None
        else:
            oldHead = self.head
            self.head = oldHead.next
            oldHead.next = None
            self.head.prev = None
            self.length -= 1
        return self

    def unshift(self, val):
        newNode = Node(val)
        if(self.head==None and self.tail==None): self.head = self.tail = newNode
        else:
            tempHead=self.head
            newNode.next=tempHead
            self.head.prev=newNode
            self.head=newNode
        self.length += 1
        return self

    def get(self, index):
        if(self.length <= 0 or index >= self.length or index < 0): return None
        mid = self.length // 2
        if index <= mid:
            temp = self.head
            for i in range(0, index+1, +1):
                if i == index: return temp
                temp = temp.next 
        elif index > mid:
            temp = self.tail
            for i in range(self.length-1, index-1, -1):
                if i == index: return temp
                temp = temp.prev

    def set(self, index, val):
        node = self.get(index)
        node.val = val
        return self

    def insert(self, index, val):
        if index < 0 or index > self.length: return None
        elif index == 0: self.unshift(val)
        elif index == self.length: self.push(val)
        else:
            node = Node(val)
            oldPrevNode = self.get(index-1)
            oldNextNode = oldPrevNode.next
            node.prev = oldPrevNode
            node.next = oldPrevNode.next
            oldPrevNode.next = node
            oldNextNode.prev = node
            self.length += 1
        return self 

    def remove(self, index):
        if index < 0 or index >= self.length: return None
        elif index == 0: return self.shift()
        elif index == self.length-1: return self.pop()
        else:
            prevNode = self.get(index-1)
            remNode = prevNode.next
            prevNode.next = remNode.next
            remNode.prev = None
            remNode.next = None
            self.length -= 1


    def traverse(self):
        if self.length == 0: return None
        else:
            current = self.head
            while(current):
                print(current.val)
                current = current.next
        

dll = DLL()

# --------------- Push test cases ---------------
# dll.push(3)
# dll.push(4)
# dll.push(5)
# print(dll.tail.prev.prev.val)

# --------------- Pop test cases ---------------
# dll.push(3)
# dll.push(4)
# dll.push(5)
# print(dll.pop())

# --------------- Shift test cases ---------------
# dll.shift()
# dll.shift()
# dll.shift()
# print(dll.head)

# --------------- UnShift test cases ---------------
# print(dll.unshift(5).head.val)
# print(dll.unshift(6).head.val)
# print(dll.unshift(7).head.val)
# print(dll.length)

# --------------- Get test cases ---------------
# dll.push("hi")
# dll.push("there")
# dll.push("omi")
# dll.push("3")
# dll.push("4")
# dll.push("5")
# dll.push("6")
# print(dll.get(0))

# --------------- Set test cases ---------------
# dll.push("hi")
# dll.push("there")
# dll.push("omi")
# print("previously:", dll.get(2).val)
# dll.set(2, "!")
# print("later:", dll.get(2).val)

# --------------- Insert test cases ---------------
# dll.push("A")
# dll.push("B")
# dll.push("C")
# dll.push("E")
# print(dll.length)
# dll.insert(3, "D")
# print(dll.length)
# dll.traverse()

# --------------- Remove test cases ---------------
# dll.push("A")
# dll.push("B")
# dll.push("C")
# dll.push("D")
# dll.traverse()
# print("------------------------------------------------")
# dll.remove(1)
# dll.traverse()