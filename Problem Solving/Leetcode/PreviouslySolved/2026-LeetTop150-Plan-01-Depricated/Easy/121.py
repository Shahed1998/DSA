class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy

        return profit


s = Solution()
s.maxProfit(prices = [7,1,5,3,6,4])
# s.maxProfit(prices = [7,6,4,3,1])
# s.maxProfit(prices = [1,2])
# s.maxProfit(prices = [3,2,3])
s.maxProfit(prices = [2,4,1])