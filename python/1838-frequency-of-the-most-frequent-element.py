class Solution1:
    """
    Key Takeaways
    -------------
    -   Sort array so next element is >= previous
    -   Sliding window
    -   Keep track of current windows sum
    -   right most pointer's element * sliding window length is
        the sum necessary to have a series of repeating elements
    -   if current window's sum + k is <= right most pointer's element
        * sliding window length, the current window is a possible
        candidate for max frequency

    Complexity Analysis
    -------------------
    Time Complexity: O(nlogn)
        -   sort: O(nlogn)
        -   sliding window: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        res = 0
        l = 0
        window_sum = 0
        for r in range(len(nums)):
            window_sum += nums[r]
            while nums[r] * (r - l + 1) > window_sum + k:
                window_sum -= nums[l]
                l += 1
            res = max(res, r - l + 1)
        return res


class Solution2:
    """
    Key Takeaways
    -------------
    -   Sort and reverse to keep track of # of operations to perform
    -   Sliding window
    -   Keep track of # of increment operations needed
    -   When # of increment operations exceed k, shift left pointer over
        -   must decrement the difference of the previous and current
            left pointer element for the entirety of the sliding window
        -   [12, 11, 10, 9, 8, 1] | k = 5
        -   ^                  ^
        -   not enough operations to include 1
        -   Shift left pointer from 12 -> 11
        -   Difference = 12 - 11 = 1
        -   Subtract 1 * length of updated sliding window from
            # of increment operations

    Complexity Analysis
    -------------------
    Time Complexity: O(nlogn)
        -   sort & reverse: O(nlogn)
        -   sliding window: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort(reverse=True)
        l = 0
        res = 1
        increments = 0
        for r in range(1, len(nums)):
            increments += nums[l] - nums[r]
            while increments > k:
                prev = nums[l]
                l += 1
                increments -= (prev - nums[l]) * (r - l + 1)
            res = max(res, r - l + 1)
        return res
