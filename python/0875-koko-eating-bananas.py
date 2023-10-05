class Solution:
    """
    Key Takeaways
    -------------
    -   Koko will not eat another pile after finishing a pile
    -   Binary search
        -   Find first True
        -   Minimum # of bananas Koko can eat = 1
        -   Maximum # of bananas Koko can eat = max(piles)
    -   Determine if Koko can eat all bananas within the given
        speed in h hours
        -   3 // 3 = 1
        -   4 // 3 = 1 => NEED 2
        -   1 // 3 = 0 => NEED 1
            -   (pile - 1) // speed + 1

    Complexity Analysis
    -------------------
    Time Complexity: O(n + logn)
        -   max(): O(n)
        -   binary search: O(logn)

    Space Complexity: O(1)
        -   no extra space required
    """
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def feasible(speed):
            res = 0
            for p in piles:
                res += (p - 1) // speed + 1
            return res <= h
            # return sum((p - 1) // speed + 1 for p in piles) <= h

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


class Solution:
    """
    Key Takeaways
    -------------
    -   Koko will not eat another pile after finishing a pile
    -   Binary search
        -   Find first False
        -   Minimum # of bananas Koko can eat = 1
        -   Maximum # of bananas Koko can eat = max(piles)
    -   Determine if Koko can eat all bananas within the given
        speed in h hours
        -   3 // 3 = 1
        -   4 // 3 = 1 => NEED 2
        -   1 // 3 = 0 => NEED 1
            -   (pile - 1) // speed + 1

    Complexity Analysis
    -------------------
    Time Complexity: O(n + logn)
        -   max(): O(n)
        -   binary search: O(logn)

    Space Complexity: O(1)
        -   no extra space required
    """
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def feasible(speed):
            res = 0
            for p in piles:
                res += (p - 1) // speed + 1
            return res > h

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if feasible(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo
