class Solution:
    """
    Key Takeaways
    -------------
    -   Gauss summation: n * (n + 1) / 2
    -   Binary search
        -   binary search to find # complete rows
        -   if gauss summation <=, then it is
            possible to create n # of complete rows
        -   Find what's not possible, and eliminate it
        -   Use upper bound to find last false (the most #
            of stairs n can create)
            [ 1,   2,   3,   4,   5 ]
            ['F', 'F', 'T', 'T', 'T']

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   binary search: O(logn)

    Space Complexity: O(1)
        -   no extra space required
    """
    def arrangeCoins(self, n: int) -> int:
        lo, hi = 1, n
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if mid * (mid + 1) / 2 > n:
                hi = mid - 1
            else:
                lo = mid
        return lo


class Solution:
    """
    Key Takeaways
    -------------
    -   Gauss summation: n * (n + 1) / 2
    -   Binary search and keep track of the max
        complete staircases

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   binary search: O(logn)
        -   max: O(1)

    Space Complexity: O(1)
        -   no extra space required
    """
    def arrangeCoins(self, n: int) -> int:
        lo, hi = 1, n
        res = 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid * (mid + 1) / 2 <= n:
                lo = mid + 1
                res = max(res, mid)
            else:
                hi = mid
        return res
