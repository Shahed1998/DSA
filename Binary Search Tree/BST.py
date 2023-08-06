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
        if self.root == None:
            self.root = node
        else:
            current = self.root
            while current:
                # Right side of the tree
                if val > current.value:
                    if current.right == None:
                        current.right = node
                        break
                    else:
                        current = current.right
                # Left side of the tree
                elif val < current.value:
                    if current.left == None:
                        current.left = node
                        break
                    else:
                        current = current.left
        return self

    # apply BST find
    def search(self, val):
        if self.root == None:
            return None
        current = self.root
        while current:
            if val == current.value:
                return current
            elif val > current.value:
                current = current.right
            elif val < current.value:
                current = current.left
        return None

    # Breadth First Search
    # Traverse the nodes horizontally
    def BFS(self):
        if self.root == None:
            return None
        queue = [self.root]
        data = []
        while len(queue) > 0:
            deq = queue.pop(0)
            data.append(deq.value)
            if deq.left:
                queue.append(deq.left)
            if deq.right:
                queue.append(deq.right)
        return data

    # Pre-order traversal
    def PreOrder(self):
        traversed = []
        current = self.root

        def helper(node):
            traversed.append(node.value)
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
        helper(current)
        return traversed

    # Post-order traversal
    def PostOrder(self):
        traversed = []
        current = self.root

        def helper(node):
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            traversed.append(node.value)
        helper(current)
        return traversed

    # In order traversal
    def InOrder(self):
        traversed = []
        current = self.root

        def helper(node):
            if node.left:
                helper(node.left)
            traversed.append(node.value)
            if node.right:
                helper(node.right)
        helper(current)
        return traversed


# ------------------------------------------------------------
# Test cases
# ------------------------------------------------------------
bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
print("PreOrder: ", bst.PreOrder())
print("InOrder: ", bst.InOrder())
print("PostOrder: ", bst.PostOrder())
