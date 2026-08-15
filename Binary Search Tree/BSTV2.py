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
                    curr.left = Node(val) # type: ignore
                    return
                else:
                    curr = curr.left
            elif val > curr.val:
                if curr.right == None:
                    curr.right = Node(val) # type: ignore
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

        return depth


    def depth_dfs(self):

        if self.root is None:
            return None

        stack = [(self.root, 1)]
        max_depth = 1

        while stack:
            node, depth = stack.pop()

            max_depth = max(max_depth, depth)

            if node.left:
                stack.append((node.left, depth+1))

            if node.right:
                stack.append((node.right, depth+1))

        return max_depth

            

bst = BST()

bst.insert(4)
bst.insert(1)
bst.insert(5)
bst.insert(3)

print(bst.depth_bfs())
print(bst.depth_dfs())