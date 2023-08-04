# ------------------------------------------------------------
# Stack using Linked List
# -------------------------------------------------------------

# class Node:

#     def __init__(self, val):
#         self.value = val
#         self.next = None

# class Stack:

#     def __init__(self):
#         self.first = None
#         self.last = None
#         self.size = 0

#     def push(self, val):
#         node = Node(val)
#         if self.size == 0:
#             self.first = node
#             self.last = self.first
#         else:
#             node.next = self.first
#             self.first = node
#         self.size += 1
#         return self.size

#     def pop(self):
#         if self.size == 0:
#             return None
#         removed = self.first
#         if self.size == 1:
#             self.first = None
#         else:
#             self.first = removed.next
#             removed.next = None
#         self.size -= 1
#         return removed.value

# ------------------------------------------------------------
# Stack using Array
# -------------------------------------------------------------

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        return

    def display(self):
        return self.stack

# ------------------------------------------------------------
# Test cases
# -------------------------------------------------------------

# s = Stack()
# s.push("A")
# s.push("B")
# s.push("C")
# print(s.display())
# s.pop()
# s.pop()
# s.pop()
# print(s.display())
