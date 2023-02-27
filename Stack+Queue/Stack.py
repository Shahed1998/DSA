class Node:

    def __init__(self, val):
        self.value = val
        self.next = None

class Stack:

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, val):
        node = Node(val)
        if self.size == 0:
            self.first = node
            self.last = self.first
        else:
            node.next = self.first
            self.first = node 
        self.size += 1
        return self.size

    def pop(self):
        if self.size == 0:
            return None
        removed = self.first
        if self.size == 1:
            self.first = None
        else:
            self.first = removed.next
            removed.next = None
        self.size -= 1
        return removed.value

# stack = Stack()
# stack.push("A")
# stack.push("B")
# stack.push("C")
# print(stack.size)
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.size)

