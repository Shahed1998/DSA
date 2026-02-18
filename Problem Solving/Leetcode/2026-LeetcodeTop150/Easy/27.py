class Solution:
    def removeElement(self, nums, val):
        i = 0
        j = len(nums) - 1

        while i <= j:
            if nums[i] != val: i += 1
            elif nums[i] == val and nums[j] != val:
                nums[i] = nums[j]
                j -= 1
                i += 1
            else: j -= 1

        # print(i)
        return i



s = Solution()
s.removeElement(nums = [3,2,2,3,3], val = 3)
s.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)