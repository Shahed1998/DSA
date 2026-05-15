class Solution:
    def maxArea(self, height):

        lptr = 0
        rptr = len(height)-1
        mc = -float('inf')

        while lptr < rptr:

            lh = min(height[lptr], height[rptr])
            mb = rptr - lptr

            mc = max(mc, lh * mb)

            if height[lptr] < height[rptr]:
                lptr += 1
            else:
                rptr -= 1

        return mc



s = Solution()
# s.maxArea(height = [1,8,6,2,5,4,8,3,7])
print(s.maxArea([8,7,2,1]))