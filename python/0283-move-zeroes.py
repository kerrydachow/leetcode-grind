class Solution:
    """
    Key Takeaways
    -------------
    -   Fast and slow pointer
    -   Slow pointer stops at 0
    -   Find 0 swap with the next non-zero number

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass

    Space Complexity: O(1)
        -   no extra space required
    """
    def moveZeroes(self, nums: list[int]) -> None:
        slow = 0
        for fast in range(1, len(nums)):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            if nums[slow] != 0:
                slow += 1
