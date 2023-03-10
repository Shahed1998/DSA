class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    # apply insert function
    def insert(self, val):
        node = Node(val)
        # when there is no root
        if(self.root == None):
            self.root = node
        else:
            current = self.root
            while(current):
                if(val > current.value and current.right == None):
                    current.right = node 
                    break
                elif (val > current.value):
                    current = current.right
                elif(val < current.value and current.left == None):
                    current.left = node
                    break
                elif (val < current.value):
                    current = current.left        
        return self
    
    # apply BST find
    def search(self, val):
        if(self.root == None):
            return None
        current = self.root
        while(current):
            if(current.value == val):
                return current
            elif(val > current.value):
                current = current.right
            elif(val < current.value):
                current = current.left
        return None
    
    # Breadth First Search
    # Traverse the nodes horizontally
    def BFS(self):
        if(self.root == None):
            return None
        queue = []
        data  = []
        queue.append(self.root)
        while(len(queue) > 0):
            deq = queue.pop(0)
            data.append(deq.value)
            if(deq.left): queue.append(deq.left)
            if(deq.right): queue.append(deq.right)
        return data

bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
print(bst.BFS())
