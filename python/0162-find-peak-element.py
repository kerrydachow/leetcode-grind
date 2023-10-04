class Solution:
    """
    Key Takeaways
    -------------
    -   Binary search find target
    -   Following the larger element will eventually lead to a peak
        -   1   2   3   4   5   6
                                ^

        -   3   1   2   3   4   5
            ^                   ^

        -   1   6   3   1   2   3
                ^

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   binary search: O(logn)

    Space Complexity: O(1)
        -   no extra space required
    """
    def findPeakElement(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mid > 0 and nums[mid - 1] > nums[mid]:
                hi = mid - 1
            elif mid < len(nums) - 1 and nums[mid + 1] > nums[mid]:
                lo = mid + 1
            else:
                return mid

class Solution:
    """
    Key Takeaways
    -------------
    -   Binary search find last False
    -   Following the larger element will eventually lead to a peak
    -   If left value is > current value, eliminate right side

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   binary search: O(logn)

    Space Complexity: O(1)
        -   no extra space required
    """
    def findPeakElement(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if nums[mid] < nums[mid - 1]:
                hi = mid - 1
            else:
                lo = mid
        return lo


class Solution:
    """
    Key Takeaways
    -------------
    -   Binary search find first false
    -   Following the larger element will eventually lead to a peak
    -   If right value > current value, eliminate left side

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   binary search: O(logn)

    Space Complexity: O(1)
        -   no extra space required
    """
    def findPeakElement(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo
