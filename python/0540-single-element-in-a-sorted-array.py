class Solution:
    """
    Key Takeaways
    -------------
    -   [(1, 1), (2), (3, 3), (4, 4), (8, 8)] - input
    -   [(0, 1), (2), (3, 4), (5, 6), (7, 8)] - indices
    -   Indices in nums will follow an even-odd rule until
        the order is broken by the single element
    -   Binary search and find the first index that
        breaks this rule
        -   [(1, 1), (2), (3, 3), (4, 4), (8, 8)] - input
        -   [(1, 1), (2), (3, 3), (4, 4), (8, 8)] - indices
        -   [(T, T), (F), (F, F), (F, F), (F, F)]

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   binary search: O(logn)

    Space Complexity: O(1)
        -   no extra space required
    """
    def singleNonDuplicate(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if (mid % 2 == 0 and nums[mid + 1] == nums[mid]) or \
                    (mid % 2 == 1 and nums[mid - 1] == nums[mid]):
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


class Solution:
    """
    Key Takeaways
    -------------
    -   Use XOR 1 to find the corresponding pair
    -   XORing a number will give us it's odd or even pair
        -   2 ^ 1 = 3
        -   3 ^ 1 = 2
        -   10 ^ 1 = 11
        -   11 ^ 1 = 10
    -   Use XOR 1 to check if the corresponding pair is
        the same value
    -   Binary search to find the first number that breaks this
        trend
    -   Find the first false whose pair isn't == current num

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   binary search: O(logn)

    Space Complexity: O(1)
        -   no extra space required
    """
    def singleNonDuplicate(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == nums[mid ^ 1]:  # check if the pair is the same
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
