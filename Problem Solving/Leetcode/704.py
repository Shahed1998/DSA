class Solution:
    def sequentialSearch(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target: return i
            elif nums[i] > target: return -1

        return -1




sln = Solution()
print(sln.search([-1,0,3,5,9,12], 9))
print(sln.search([-1,0,3,5,9,12], 2))