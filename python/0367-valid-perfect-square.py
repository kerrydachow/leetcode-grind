class Solution:
    """
    Key Takeaways
    -------------
    -   Binary search to find the closest integer to square
    -   Find first false

    ['T', 'T', 'T', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F']
    [ 1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16 ]
                     ^

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   binary search: O(logn)

    Space Complexity: O(1)
        -   no extra space required
    """
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 1, num
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid ** 2 < num:
                lo = mid + 1
            else:
                hi = mid
        return lo ** 2 == num


class Solution:
    """
    Key Takeaways
    -------------
    -   Binary search to find the closest integer to square
    -   Find first true

    ['F', 'F', 'F', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T']
    [ 1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16 ]
                     ^

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   binary search: O(logn)

    Space Complexity: O(1)
        -   no extra space required
    """
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 1, num
        print(["T" if x ** 2 >= num else "F" for x in range(1, num)])
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid ** 2 >= num:
                hi = mid
            else:
                lo = mid + 1
        return lo ** 2 == num


class Solution:
    """
    Key Takeaways
    -------------
    -   Binary search to find the closest integer to square
    -   Find last false

    ['F', 'F', 'F', 'F', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T']
    [ 1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16 ]
                     ^

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   binary search: O(logn)

    Space Complexity: O(1)
        -   no extra space required
    """
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 1, num
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if mid ** 2 > num:
                hi = mid - 1
            else:
                lo = mid
        return lo ** 2 == num



class Solution:
    """
    Key Takeaways
    -------------
    -   Binary search to find the closest integer to square
    -   Find last true

    ['T', 'T', 'T', 'T', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F']
    [ 1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16 ]
                     ^

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   binary search: O(logn)

    Space Complexity: O(1)
        -   no extra space required
    """
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 1, num
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if mid ** 2 <= num:
                lo = mid
            else:
                hi = mid - 1
        return lo ** 2 == num
