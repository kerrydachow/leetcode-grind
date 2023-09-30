class Solution1:
    """
    Key Takeaways
    -------------
    -   Dictionary operation: if _ in dict is O(1)
    -   Set operation: if _ in set is O(1)
    -   Store elements in dictionary/set during iteration
    -   Check if element has been stored in dictionary/set

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass through nums

    Space Complexity: O(n)
        -   dictionary / set storing nums
    """
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = True
        return False


class Solution2:
    """
    Key Takeaways
    -------------
    -   Set data structure is a collection of unique data (no duplicates)

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   built-in set() function

    Space Complexity: O(n)
        -   set data structure
    """
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)


class Solution3:
    """
    Key Takeaways
    -------------
    -   Sort in-place with list.sort() method
    -   Memory efficient

    Complexity Analysis
    -------------------
    Time Complexity: O(nlogn)
        -   built-in method sort

    Space Complexity: O(1)
        -   built-in method sort is in-place
    """
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()  # O(nlogn)
        prev = nums[0]
        for num in nums[1:]:
            if num == prev:
                return True
            else:
                prev = num
        return False
