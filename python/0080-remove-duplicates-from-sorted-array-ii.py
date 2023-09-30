class Solution1:
    """
    Key Takeaways
    -------------
    -   Two pointer approach
    -   Check if there is a group of 3
    -   Begin checking for groups of 3 after slow pointer reaches index 2
    -   If a group of 3 has been detected, it needs to be overwritten
        in the future -- continue incrementing i
    -   Increment slow pointer after replaced because group of 3
        has been resolved

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass

    Space Complexity: O(1)
        -   no extra space required
    """
    def removeDuplicates(self, nums: list[int]) -> int:
        j = 0
        for i in range(len(nums)):
            if j < 2 or nums[i] > nums[j - 2]:
                # No group of 3, increment
                nums[j] = nums[i]
                j += 1
        return j


class Solution2:
    """
    Key Takeaways
    -------------
    -   Same concept as above, but while-loop

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass

    Space Complexity: O(1)
        -   no extra space required
    """
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        i, j = 2, 2
        while i < len(nums):
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j
