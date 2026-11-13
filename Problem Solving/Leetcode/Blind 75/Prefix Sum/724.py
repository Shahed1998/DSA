class Solution:
    def pivotIndex(self, nums):

        # Crazy solution 
        total = sum(nums)
        leftSum = 0

        for i,n in enumerate(nums):

            # Check if the left sum is equal to the right sum
            if leftSum == total - leftSum - n:
                return i

            leftSum += n

        return -1

        # prefix_sum = 0
        # res = []
        # leftmost_zero = -1

        # for i in range(len(nums)):
        #     res.append(prefix_sum)
        #     prefix_sum += nums[i]

        # suffix_sum = 0

        # for i in range(len(nums)-1, -1, -1):

        #     res[i] -= suffix_sum

        #     if res[i] == 0:
        #         leftmost_zero = i

        #     suffix_sum += nums[i]

        # return leftmost_zero

        






s = Solution()
print(s.pivotIndex(nums = [1,7,3,6,5,6]))
print(s.pivotIndex(nums = [1,2,3]))
print(s.pivotIndex(nums = [2,1,-1]))