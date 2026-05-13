class Solution:
    def moveZeroes(self, nums):
        slow = 0
        
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

        print(nums)



            



        


s = Solution()
s.moveZeroes([1,0,3,0,0,1,0,3,12])