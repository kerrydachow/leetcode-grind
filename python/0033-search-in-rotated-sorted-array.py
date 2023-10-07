class Solution:
    """
    Key Takeaways
    -------------
    -   Binary search find exact target
    -   Check if we are in rotated or non-rotated portion
    -   Ensure target is between the range of the portion
        -   else eliminate the current portion

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   binary search: O(logn)

    Space Complexity: O(1)
        -   no extra space required
    """
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[hi]:
                if nums[mid] > target >= nums[lo]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
