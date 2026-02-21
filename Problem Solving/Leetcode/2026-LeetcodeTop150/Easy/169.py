class Solution:
    def majorityElement(self, nums):
        # Phase 1: Initialize the first element as our "Champion"
        elem = nums[0]
        count = 1

        for i in range(1, len(nums)):
            # Phase 2: The "Tug-of-War"
            # If the current number matches the champion, strengthen it (+1)
            # If it's different, weaken the champion (-1)
            if nums[i] != elem:
                count -= 1
            else:
                count += 1

            # Phase 3: Replacement
            # If the champion's count is depleted, the current 
            # number takes over as the new champion.
            if count < 0:
                elem = nums[i]
                count = 1

        # The majority element (appearing > n/2 times) is 
        # mathematically guaranteed to be the last one standing.
        return elem

s = Solution()
# s.majorityElement(nums = [3,2,3])
# s.majorityElement(nums = [2,2,1,1,1,2,2])
s.majorityElement(nums = [6,6,6,7,7])
        
# Summary
# Algorithm name: Boyer-Moore Majority Vote Algorithm.
# The Goal: Find the element that appears more than 50% of the time.
# The Logic: Every "non-majority" element can be paired with a "majority" element to cancel each other out. Since the majority element has more than 50% of the "votes,"
# it will always have at least one vote left over after all cancellations.
# Time: O(n) (One pass).
# Space: O(1) (No extra arrays/hashmaps).