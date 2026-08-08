class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None
        self.depth = 0


    def insert(self, val):

        if self.root == None:
            self.root = Node(val)
            return

        curr = self.root

        while(curr):

            if val < curr.val:
                if curr.left == None:
                    curr.left = Node(val)
                    return
                else:
                    curr = curr.left
            elif val > curr.val:
                if curr.right == None:
                    curr.right = Node(val)
                    return
                else:
                    curr = curr.right
            else:
                return


    def bfs(self):

        if self.root == None:
            return None



bst = BST()

bst.insert(4)
bst.insert(2)