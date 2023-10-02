class Solution:
    """
    Key Takeaways
    -------------
    -   Binary search find exact target
    -   [-1,   0,   3,   5,   9,   12] | target = 9
    -   ['F', 'F', 'F', 'F', 'T', 'F']

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   binary search: O(log n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1


class Solution:
    """
    Key Takeaways
    -------------
    -   Binary search lower bound
    -   Find the first false value
    -   [-1,   0,   3,   5,   9,   12] | target = 9
    -   ['T', 'T', 'T', 'T', 'F', 'F']

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   binary search: O(logn)

    Space Complexity: O(1)
        -   no extra space required
    """
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo if nums[lo] == target else -1


class Solution:
    """
    Key Takeaways
    -------------
    -   Binary search upper bound
    -   Find the last false value
    -   [-1,   0,   3,   5,   9,   12] | target = 9
    -   ['F', 'F', 'F', 'F', 'F', 'T']

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   binary search: O(logn)

    Space Complexity: O(1)
        -   no extra space required
    """
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid
        return lo if nums[lo] == target else -1
