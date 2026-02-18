class Solution:
    def merge(self, nums1, m, nums2, n) -> None:

        i = m-1
        j = n-1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        print(nums1)

s = Solution()

s.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
s.merge(nums1 = [1], m = 1, nums2 = [], n = 0)
s.merge(nums1 = [0], m = 0, nums2 = [1], n = 1)


# PROBLEM:
# nums1 has length m + n
# - first m elements are valid and sorted
# - last n elements are empty (0) just for space
# nums2 has n elements and is sorted
# Goal: merge nums2 into nums1 in-place, sorted

# CORE IDEA:
# Always merge from the END of nums1.
# Why?
# - The largest values are at the end of both arrays
# - nums1 has free space at the end
# - This avoids overwriting useful data

# POINTER SETUP:
# i = m - 1        -> last valid element of nums1
# j = n - 1        -> last element of nums2
# k = m + n - 1    -> last position of nums1 (empty slot)

# MAIN LOOP:
# While both arrays still have elements:
# - Compare nums1[i] and nums2[j]
# - Place the larger one at nums1[k]
# - Move the pointer of the array you used
# - Always move k backward

# WHY THIS IS SAFE:
# - nums1[k] is always an empty slot OR already used
# - we never overwrite a value before using it

# AFTER MAIN LOOP:
# Two possibilities:

# Case 1: nums2 is finished first (j < 0)
# - Remaining nums1 elements are already in correct place
# - Nothing to do

# Case 2: nums1 is finished first (i < 0)
# - nums1 has no valid elements left
# - Copy remaining nums2 elements into nums1
# - This is safe because only empty positions remain

# IMPORTANT RULE:
# We NEVER need to copy remaining nums1 elements
# because they are already sorted and positioned correctly

# TIME COMPLEXITY:
# O(m + n) -> each element is processed once

# SPACE COMPLEXITY:
# O(1) -> in-place merge, no extra array used
