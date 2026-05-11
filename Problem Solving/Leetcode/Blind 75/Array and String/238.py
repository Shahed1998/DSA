class Solution:
    def productExceptSelf(self, nums):

        #-----------------------------------------------------------
        # Optimal solution: prefix product * suffix product
        #-----------------------------------------------------------

        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix # suffix is multiplied because prefix is already stored in the index
            suffix *= nums[i]


        return res



        #-----------------------------------------------------------
        # Un-optimal solution: Constraint not met
        # division was not allowed
        #-----------------------------------------------------------
        # countZero = 0
        # product = 1

        # for num in nums:

        #     if num == 0:
        #         countZero += 1
        #         continue

        #     product *= num

        # for i in range(len(nums)):

        #     if countZero > 1:
        #         nums[i] = 0
        #         continue

        #     if countZero == 1:
        #         if nums[i] != 0:
        #             nums[i] = 0
        #         else:
        #             nums[i] = product
        #         continue

        #     nums[i] = int(product / nums[i])

        # return nums


            


        





s = Solution()
# s.productExceptSelf(nums = [-1,1,0,-3,3])
# s.productExceptSelf(nums = [1,2,3,4])
print(s.productExceptSelf(nums = [10,6,4,2]))