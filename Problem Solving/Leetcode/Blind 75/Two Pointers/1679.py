class Solution:
    def maxOperations(self, nums, k):
        op = 0
        seen = {}

        for num in nums:

            target = k - num

            if seen.get(target, 0) > 0:
                op += 1
                seen[target] -= 1
            else:
                seen[num] = seen.get(num, 0) + 1

        return op





s = Solution()
# print(s.maxOperations(nums = [1,2,3,4], k = 5))
# print(s.maxOperations(nums = [3,1,3,4,3], k = 6))
print(s.maxOperations(nums=[4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], k=2))
        