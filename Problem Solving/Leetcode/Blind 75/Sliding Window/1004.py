class Solution:
    def longestOnes(self, nums, k): 
        
        left = 0
        countZeros = 0
        maxLen = 0

        for right in range(len(nums)):
            
            if nums[right] == 0:
                countZeros += 1

            while countZeros > k:

                if nums[left] == 0:
                    countZeros -= 1 

                left += 1

            maxLen = max(maxLen, right-left+1)

        return maxLen


            







s = Solution()
s.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2)
s.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3)