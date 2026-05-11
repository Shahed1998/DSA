class Solution:
    def increasingTriplet(self, nums):
        
        first = float('inf')
        second = float('inf')

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