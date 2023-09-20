class Solution:
    """
    Key Takeaways
    -------------
    -   Sliding window
    -   Think inverse => Maximum Subarray of sum(nums) - x
    -   Set res to -1 to determine if target was ever found

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   sum(): O(n)
        -   sliding window: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        res = -1
        l = 0
        curr_sum = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while l <= r and curr_sum > target:
                curr_sum -= nums[l]
                l += 1
            if curr_sum == target:
                res = max(res, r - l + 1)
        return -1 if res == -1 else len(nums) - res
