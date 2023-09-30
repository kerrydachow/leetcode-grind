class Solution:
    """
    Key Takeaways
    -------------
    -   Sliding window
    -   Set one pointer on min price
    -   Second pointer iterates through prices
    -   Move first pointer if new min price found
    -   Else check if today is a better profit

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass

    Space Complexity: O(1)
        -   no extra space required
    """
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for price in prices[1:]:
            if price < buy:
                buy = price
            elif price > buy:
                max_profit = max(max_profit, price - buy)
        return max_profit
