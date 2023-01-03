class Solution:
    """
    121. Best Time to Buy and Sell Stock

    You are given an array prices where prices[i] is the price of a
    given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy
    one stock and choosing a different day in the future to sell that
    stock.

    Return the maximum profit you can achieve from this transaction.
    If you cannot achieve any profit, return 0.
    """
    def maxProfit(self, prices: list[int]) -> int:
        """
        >>> Solution().maxProfit([7,1,5,3,6,4])
        5
        >>> Solution().maxProfit([7,6,4,3,1])
        0
        """
        buy, sell, profit = 0, 1, 0
        while sell < len(prices):
            current_profit = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                profit = max(profit, current_profit)
            else:
                buy = sell
            sell += 1
        return profit

