class Solution:
    def containsNearbyDuplicate(self, nums, k):

        hashMap = {}
        result = False

        for i in range(len(nums)):

            if nums[i] in hashMap and i - hashMap[nums[i]] <= k:
                result = True
                break

            hashMap[nums[i]] = i

        return result





s = Solution()
print(s.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
print(s.containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
print(s.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))
print(s.containsNearbyDuplicate(nums = [0,1,2,3,2,5], k = 3))

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.