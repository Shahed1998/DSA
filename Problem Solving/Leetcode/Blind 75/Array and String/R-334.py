class Solution:
    def increasingTriplet(self, nums):
        
        first = float('inf')
        second = float('inf')

        # the first and second smallest number is extracted. And if there exists a number bigger than first and second then Triplet is found
        # E.g. - 1 < 2 < 3
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False 

 

s = Solution()
print(s.increasingTriplet([ 5, 2, 2147483647,1,4,2, 2147483649]))