class Solution1:
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
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[j - 1]:
                nums[j] = nums[i]
                j += 1
        return j


class Solution2:
    """
    Key Takeaways
    -------------
    -   Two pointers, one starts at 0, another at 1
    -   Array is sorted
    -   Pointer i iterates through nums
    -   Pointer j stays at the previous unique number until i
        points to a value that is not equal to j
    -   Increment j to the position to place the next unique element

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass
    Space Complexity: O(1)
        -   no extra space required
    """
    def removeDuplicates(self, nums: list[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1
