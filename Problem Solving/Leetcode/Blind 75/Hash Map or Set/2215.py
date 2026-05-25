class Solution:
    def findDifference(self, nums1, nums2):
        sNums1 = set(nums1)
        sNums2 = set(nums2)

        return [list(sNums1.difference_update(sNums2)), list(sNums2.difference_update(sNums1))] #using set difference

        

        


s = Solution()
print(s.findDifference([1,2,3,3], [1,1,2,2]))
print(s.findDifference(nums1 = [1,2,3], nums2 = [2,4,6]))