class Solution:
    """
    Key Takeaways
    -------------
    -   Binary search lower bound
        -   upper bound won't work because we are:
            1.  extending UPPER search range -> out of bounds error
            2.  if target does not exist, returns lower index of
                where target should have been located

        -   upper bound
                Find last False value
                "Which values are > target?"
                [ 1,   3,   5,   6 ] | target = 2
                ['F', 'T', 'T', 'T']
                  ^
        -   lower bound
            -   Find first False value
            -   "Which values are < target?"
                [ 1,   3,   5,   6 ] | target = 2
                ['T', 'F', 'F', 'F']

    -   Edge case of target being the last index
        -   extend the search range to include
            last index + 1

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   binary search: O(logn)

    Space Complexity: O(1)
        -   no extra space required
    """
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo
