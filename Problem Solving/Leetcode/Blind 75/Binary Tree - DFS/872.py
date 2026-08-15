# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1, root2) -> bool:

        leaves01 = []
        leaves02 = []
        
        def getLeaves(node, leaves):

            if node is None:
                return

            getLeaves(node.left, leaves)

            if node.right is None and node.left is None: leaves.append(node.val)

            getLeaves(node.right, leaves)

        getLeaves(root1, leaves01)
        getLeaves(root2, leaves02)

        return (leaves01 == leaves02)





        



        