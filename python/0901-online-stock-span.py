class StockSpanner:
    """
    Key Takeaways
    -------------
    -   Monotonic decreasing stack
    -   Consume all previous smaller stocks
        -   accumulate the count
    -   Push current price, and # of consumed stocks + 1 to stack
    -   Stack will maintain a monotonic decreasing price

    Complexity Analysis
    -------------------
    Time Complexity: O(1)
        -   Amortized time complexity: O(1)
            -   some cases will have a higher time complexity
            -   resulting in TLE

    Space Complexity: O(n)
        -   store previous stocks: O(n)
    """
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res
