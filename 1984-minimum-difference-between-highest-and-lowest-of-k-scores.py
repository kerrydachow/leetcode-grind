class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        """
        Key Takeaways
        -------------
        -   Minimum possible difference of a window of length k
        -   Sort the array
        -   The closer the numbers are in value, the smaller
            the difference will be

        Complexity Analysis
        -------------------
        Time Complexity: O(nlogn)
            -   sort: O(nlogn)
            -   one pass: O(n)

        Space Complexity: O(1)
            -   no extra space required
        """
        nums.sort()
        i = 0
        res = float("inf")
        for j in range(k - 1, len(nums)):
            res = min(res, nums[j] - nums[i])
            i += 1
        return res
