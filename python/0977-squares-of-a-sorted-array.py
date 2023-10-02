class Solution:
    """
    Key Takeaways
    -------------
    -   When a negative number gets squared, it becomes positive
    -   Two pointers
    -   Build output array from n'th index until 0
    -   The largest squared elements will be either
        the first or last index

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   create output array: O(n)
        -   iterate through nums reversed: O(n)

    Space Complexity: O(1)
        -   output array: O(n)
    """
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = [0] * len(nums)
        l, r = 0, len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[r]) > abs(nums[l]):
                res[i] = nums[r] ** 2
                r -= 1
            else:
                res[i] = nums[l] ** 2
                l += 1
        return res
