class Solution:
    """
    Key Takeaways
    -------------
    -   Sort the input array
    -   Subsequences of sorted input and non-sorted input stay the same
    -   Sorted array allows us to easily eliminate elements that are too
        large
    -   Count # of subsequences between nums[i+1:j] where nums[i] + nums[j]
        is <= target

    Complexity Analysis
    -------------------
    Time Complexity: O(nlogn)
        -   sort array first
        -   iterate through with 2 pointers: O(n)
            -   while loop to decrement j pointer

    Space Complexity: O(n)
        -   no extra space required
    """
    def numSubseq(self, nums: list[int], target: int) -> int:
        nums.sort()
        mod = 10**9 + 7
        res = 0
        j = len(nums) - 1
        for i in range(len(nums)):
            while nums[i] + nums[j] > target and i <= j:
                j -= 1
            if i <= j:
                res += 2 ** (j - i)
                res %= mod
        return res
