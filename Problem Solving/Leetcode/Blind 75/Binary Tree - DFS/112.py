class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:

        if root is None:
            return False

        if not root.right and not root.left:
            return targetSum == root.val

        remaining = targetSum - root.val

        return (self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining))
        