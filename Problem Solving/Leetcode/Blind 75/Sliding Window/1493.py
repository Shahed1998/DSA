class Solution:
    def longestSubarray(self, nums):

        left = 0
        countZero = 0
        maxLen = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                countZero += 1

            while countZero > 1:

                if nums[left] == 0:
                    countZero -= 1

                left += 1

            maxLen = max(maxLen, right-left)

        return maxLen
            

            



s = Solution()
s.longestSubarray(nums = [1,1,0,1])
s.longestSubarray(nums = [1,1,1])
        