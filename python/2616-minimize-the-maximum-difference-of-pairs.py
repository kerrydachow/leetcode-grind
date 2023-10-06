class Solution:
    """
    Key Takeaways
    -------------
    -   Binary search to find the minimum maximum difference
        -   Find the first False
        -   Guess a random minimum maximum difference (threshold)
            between 0 and difference of max(nums) - min(nums)
        -   Count the # of pairs possible with this threshold
        -   Return True if we can't form >= p # of pairs
            -   First False will be the MINIMUM maximum difference
    -   Sort nums to greedy search
    -   The minimum difference will be neighboring numbers
        that are pairs

    Complexity Analysis
    -------------------
    Time Complexity: O(nlogn + logm)
        -   sort(): O(nlogn)
        -   binary search in range max(nums) - min(nums): O(logm)

    Space Complexity: O(1)
        -   no extra space required
    """
    def minimizeMax(self, nums: list[int], p: int) -> int:
        def not_feasible(threshold):
            pairs = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= threshold:
                    pairs += 1
                    i += 1
                i += 1
            return pairs < p

        nums.sort()
        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if not_feasible(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo


class Solution:
    """
    Key Takeaways
    -------------
    -   Binary search to find the minimum maximum difference
        -   Find the first True
        -   Guess a random minimum maximum difference (threshold)
            between 0 and difference of max(nums) - min(nums)
        -   Count the # of pairs possible with this threshold
        -   Return False if we can't form >= p # of pairs
            -   First True will be the MINIMUM maximum difference
    -   Sort nums to greedy search
    -   The minimum difference will be neighboring numbers
        that are pairs

    Complexity Analysis
    -------------------
    Time Complexity: O(nlogn + logm)
        -   sort(): O(nlogn)
        -   binary search in range max(nums) - min(nums): O(logm)

    Space Complexity: O(1)
        -   no extra space required
    """
    def minimizeMax(self, nums: list[int], p: int) -> int:
        def feasible(threshold):
            pairs = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= threshold:
                    pairs += 1
                    i += 1
                i += 1
            return pairs >= p

        nums.sort()
        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
