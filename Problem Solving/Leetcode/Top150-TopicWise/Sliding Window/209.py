class Solution:
    def minSubArrayLen(self, target, nums):
        # optimal solution
        left = 0
        total = 0
        window = len(nums)+1

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                window = min(window, right-left+1)
                total -= nums[left]
                left += 1 

        return 0 if window == len(nums)+1 else window



s = Solution()
print(s.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
print(s.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))
