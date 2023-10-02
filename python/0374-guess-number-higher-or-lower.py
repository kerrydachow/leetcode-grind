class Solution:
    """
    Key Takeaways
    -------------
    -   Lower bound binary search
    -   Number we're searching for exists
    -   Use lower mid
        -   else-clause sets hi to lower mid
        -   therefore no infinite loop
    -   Finds first false

        "Is x < ans?"
        ans = 6
        1   2   3   4   5   6   7   8   9
        T   T   T   T   T   F   F   F   F

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   binary search

    Space Complexity: O(1)
        -   no extra space required
    """
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if guess(mid) == 1:
                lo = mid + 1
            else:
                hi = mid
        return lo


class Solution:
    """
    Key Takeaways
    -------------
    -   Upper bound binary search
    -   Number we're searching for exists
    -   Use upper mid
        -   else-clause must set lo to upper mid
        -   therefore no infinite loop
    -   Finds last false

        "Is x > ans?"
        ans = 6
        1   2   3   4   5   6   7   8   9
        F   F   F   F   F   F   T   T   T

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   binary search

    Space Complexity: O(1)
        -   no extra space required
    """
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if guess(mid) == -1:
                hi = mid - 1
            else:
                lo = mid
        return lo

class Solution:
    """
    Key Takeaways
    -------------
    -   Binary search find exact
    -   Number we're searching for exists
    -   Find first True
        "Is x == ans?"
        ans = 6
        1   2   3   4   5   6   7   8   9
        F   F   F   F   F   T   F   F   F

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   binary search: O(logn)

    Space Complexity: O(1)
        -   no extra space required
    """
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if guess(mid) == -1:
                hi = mid - 1
            elif guess(mid) == 1:
                lo = mid + 1
            else:
                return mid


def guess(num: int) -> int:
    pass
