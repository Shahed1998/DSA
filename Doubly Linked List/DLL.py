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