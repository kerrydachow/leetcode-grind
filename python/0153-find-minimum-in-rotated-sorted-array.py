class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Key Takeaways
        -------------
        -   Determine which portion of the array we are in
            -   Rotated portion
            -   Non-rotated portion
            -   compare current element to last element
                -   if curr > last, we are in rotated
                -   if curr < last, we are in non-rotated
        -   Binary search find first False
            -   if we are not in rotated portion:
                -   eliminate mid + 1 -> hi

        Complexity Analysis
        -------------------
        Time Complexity: O(logn)
            -   binary search: O(logn)

        Space Complexity: O(1)
            -   no extra space required
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[-1]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
