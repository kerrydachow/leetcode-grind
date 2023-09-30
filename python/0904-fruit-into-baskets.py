class Solution:
    """
    Key Takeaways
    -------------
    -   Sliding window
    -   Maintain a basket with the count of fruit
    -   If 3 baskets are necessary, start removing fruit from the
        left pointer
    -   length of sliding window = # of fruits in baskets

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   sliding window: O(n)

    Space Complexity:
        -   O(1)
            -   dictionary of at most 3 items
    """
    def totalFruit(self, fruits: list[int]) -> int:
        baskets = {}
        res = 0
        l = 0
        for r in range(len(fruits)):
            baskets[fruits[r]] = baskets.get(fruits[r], 0) + 1
            while len(baskets) > 2:
                baskets[fruits[l]] -= 1
                if baskets[fruits[l]] == 0:
                    del baskets[fruits[l]]
                l += 1
            res = max(res, r - l + 1)
        return res
