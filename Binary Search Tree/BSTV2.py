class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None
        
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


    def depth_bfs(self):

        if self.root == None:
            return None

        queue  = [self.root]
        res = []
        depth = 0

        while queue:

            depth += 1
            next_queue = []

            for node in queue:

                res.append(node.val)

                if node.left:
                    next_queue.append(node.left)

                if node.right:
                    next_queue.append(node.right)

            queue = next_queue

        print(depth, res)

            






bst = BST()

bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
bst.depth_bfs()