class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 1: return len(nums)

        i=0; j=1

        while j < len(nums):
            if nums[j] != nums[i]: 
                i += 1
                nums[i] = nums[j]

            j += 1
        
        return i + 1
        

s = Solution()
s.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4])

# I have solved it myself
# Since the array is sorted, duplicates will always be adjacent. 
# I use two pointers: one pointer i tracks the position of the last unique element, and another pointer j scans the array. 
# Whenever I find a new unique element at j, I increment i and copy that element to position i. This ensures the first k elements are unique. 
# The algorithm runs in O(n) time and O(1) space since it modifies the array in place.