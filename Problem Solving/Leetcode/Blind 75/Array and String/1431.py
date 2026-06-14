class Solution:
    def kidsWithCandies(self, candies, extraCandies):

        maxCandy = 0

        for totalCandy in candies:
            maxCandy = totalCandy if totalCandy > maxCandy else maxCandy

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandy: candies[i] = True
            else: candies[i] = False

        return candies

        

s = Solution()
s.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3)
s.kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1)
s.kidsWithCandies(candies = [12,1,12], extraCandies = 10)