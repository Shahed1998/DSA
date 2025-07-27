def maxProfit(prices):

    buy_price = prices[0]
    profit = 0

    for i in range(1, len(prices)):

        if prices[i] < buy_price: buy_price = prices[i]

        if prices[i] - buy_price > profit: profit = prices[i] - buy_price


    return profit

    




print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
print(maxProfit([2,4,1]))
print(maxProfit([2,1,4]))