class Solution:
    """
    Key Takeaways
    -------------
    -   Two pointers start at index 1
        -   first element is always unique
    -   Array is sorted
    -   If i'th element == j-1'th element, continue
    -   If i'th element != j-1'th element, nums[i] = nums[j]
    -   j will always be the index to place the next unique element
    -   j is the # of unique elements

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass
    Space Complexity: O(1)
        -   no extra space required
    """
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 1
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[j - 1]:
                nums[j] = nums[i]
                j += 1
        return j
