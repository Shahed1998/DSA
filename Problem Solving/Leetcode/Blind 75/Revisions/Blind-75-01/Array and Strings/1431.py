class Solution:
    def kidsWithCandies(self, candies, extraCandies):

        max_candies = 0
        result = []

        for c in candies: max_candies = max(max_candies, c)

        for i in range(len(candies)): 
            result.append(candies[i] + extraCandies >= max_candies)

        return result

  


s = Solution()
print(s.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))