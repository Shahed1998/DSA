class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # push
    def push(self, val):
        newNode = Node(val)
        if not self.head: 
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
        
        self.length += 1
        return self

    # traverse a linked list
    def traverse(self):
        currentValue = self.head
        while(currentValue):
            print(currentValue.val)
            currentValue = currentValue.next
        return None 

    # pop from a linked list
    def pop(self):
        if not self.head: return None
        current = self.head
        newTail = current
        while current.next:
            newTail = current
            current = current.next
        self.tail = newTail
        self.tail.next = None
        self.length -= 1
        if(self.length == 0):
            self.head = None
            self.tail = None
        return current.val

    # remove item from the front of a linked list
    def shift(self):
        if not self.head: return None
        current = self.head
        if not current.next:
            self.head = None
            self.tail = None
            self.length -= 1
            return current    
        self.head = current.next
        self.length -= 1
        return current

    # add node at the beginning of the list
    def unShift(self,val):
        if not self.head:
            self.push(val)
        else:
            newHead = Node(val)
            newHead.next = self.head
            self.head = newHead
            self.length += 1
        return self

    # Get the element at the specific index of the linked list
    def get(self, index):
        if index < 0 or index >= self.length: return None
        currentNode = self.head
        currentIndex = 0
        while(currentIndex < index):
            currentNode = currentNode.next
            currentIndex += 1
        return currentNode

    # Set 
    def set(self, index, value):
        nd = self.get(index)
        if nd: 
            nd.val = value
            return self
        return None

    # Insert
    def insert(self, index, value):

        if index > self.length or index < 0: return False

        elif index == self.length: self.push(value)

        elif index == 0: self.unShift(value)

        else:

            node = Node(value)

            temp = self.get(index - 1)

            tempIndex = temp.next

            temp.next = node

            node.next = tempIndex

            self.length += 1

            return self

    # Remove
    def remove(self, index):

        if (index >= self.length or index < 0): return None

        elif (index == 0): return self.shift()

        else:

            prev = self.get(index -1)

            rem = prev.next

            prev.next = rem.next

            self.length -= 1

            self.traverse()

        print("--------------------")

        return self  

    # Reverse

    def reverse(self):

        #converting head to tail
        newTail = self.head
        oldTail = self.tail
        self.head = self.head.next
        newTail.next = None
        oldTail.next = newTail


        for i in range(self.length-2):
            newTailPtr = oldTail.next
            oldTail.next = self.head
            newHeadPtr = self.head.next
            self.head = newHeadPtr
            oldTail.next.next = newTailPtr

        self.traverse()
        

# --------------------------------- Test cases ---------------------------------
sll = SinglyLinkedList()

# PUSH OPERATION

sll.push("a")
sll.push("b")
sll.push("c")
sll.push("d")
sll.push("e")

# TRAVERSE OPERATION

sll.traverse()

print("--------------------")

sll.reverse()