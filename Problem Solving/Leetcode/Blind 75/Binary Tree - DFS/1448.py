class Solution:
    def goodNodes(self, root) -> int:

        def dfs(currNode, maxSoFar):

            if currNode is None: return 0

            count = 1 if currNode.val >= maxSoFar else 0
            newMax = max(maxSoFar, currNode.val)

            count += dfs(currNode.left,  newMax)
            count += dfs(currNode.right, newMax)

            return count

        return dfs(root, root.val)