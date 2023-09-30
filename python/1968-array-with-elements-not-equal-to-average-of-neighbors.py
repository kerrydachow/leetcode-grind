class Solution:
    """
    Key Takeaways
    -------------
    -   Sort array
    -   middle element cannot equal average of its neighbours
        if the pattern [bigger, smaller, bigger] or
        [smaller, bigger, smaller] persists

    Complexity Analysis
    -------------------
    Time Complexity: O(nlogn)
        -   sort: O(nlogn)
        -   iterate through nums: O(n)

    Space Complexity: O(1)
        -   modify in-place
    """
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        nums.sort()
        i, j = 1, 2
        while j < len(nums):
            nums[j], nums[i] = nums[i], nums[j]
            j += 2
            i = j - 1
        return nums
