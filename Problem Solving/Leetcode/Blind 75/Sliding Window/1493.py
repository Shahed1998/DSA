class Solution:
    def longestSubarray(self, nums):

        countZero = 0
        left = 0
        maxSize = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                countZero += 1

            while countZero > 1:

                if nums[left] == 0:
                    countZero -= 1

                left += 1

            maxSize = max(maxSize, right-left+1-1) # -1 because we must delete one element from the window

        return maxSize
            

            



s = Solution()
s.longestSubarray(nums = [1,1,0,1])
s.longestSubarray(nums = [1,1,1])
        