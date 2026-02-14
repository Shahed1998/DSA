class Solution:
    def merge(self, nums1, m, nums2, n) -> None:

        x = m

        for i in nums2:
            nums1[x] = i
            x += 1
        
        while n < len(nums1):
            print('TBC...')


s = Solution()

s.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)