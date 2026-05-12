class Solution:
    def moveZeroes(self, nums):
        lptr = 0
        rptr = len(nums)-1

        while lptr < rptr:

            if nums[lptr] == 0:
                nums[lptr], nums[rptr] = nums[rptr], nums[lptr]
                rptr -= 1
            
            lptr += 1

        print(nums)
        


s = Solution()
s.moveZeroes([0,1,0,3,12])