class Solution:
    """
    Key Takeaways
    -------------
    -   Binary search to find lower bound
    -   Binary search to find upper bound
    -   Check if input is empty

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   binary search lower: O(logn)
        -   binary search upper: O(logn)

    Space Complexity: O(1)
        -   no extra space required
    """
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]
        return [self.searchLower(nums, target), self.searchUpper(nums, target)]

    def searchLower(self, nums: list[int], target: int):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo if nums[lo] == target else -1

    def searchUpper(self, nums: list[int], target: int):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid
        return lo if nums[lo] == target else -1
