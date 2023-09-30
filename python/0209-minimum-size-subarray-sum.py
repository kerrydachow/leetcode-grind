class Solution:
    """
    Key Takeaways
    -------------
    -   Sliding window
    -   Sliding window will never be > len(nums) + 1
    -   Keep track of current sum
    -   While curr_sum >= target
        -   subtract left pointer value from curr_sum
        -   shift left pointer
        -   compare length of sliding window
    -   Check if sliding window is == len(nums) + 1 >> ret 0

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   sliding window: O(n)

    Space Complexity: O(1)
        - no extra space required
    """
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        res = len(nums) + 1
        l = 0
        curr_sum = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                curr_sum -= nums[l]
                res = min(res, r - l + 1)
                l += 1
        return res if res != len(nums) + 1 else 0
