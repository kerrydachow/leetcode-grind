class Solution:
    """
    217. Contains Duplicate

    Given an integer array nums, return true if any value appears at
    least twice in the array, and return false if every element is
    distinct.
    """
    def contains_duplicate_bf(self, nums: list[int]) -> bool:
        """
        Brute Force
        -----------
        Iterate through every element and compare with the other elements.

        >>> Solution().contains_duplicate_bf([1,2,3,1])
        True
        >>> Solution().contains_duplicate_bf([1,2,3,4])
        False
        >>> Solution().contains_duplicate_bf([1,1,1,3,3,4,3,2,4,2])
        True
        """
        for i_index, i in enumerate(nums):
            for j_index, j in enumerate(nums):
                if i_index != j_index and i == j:
                    return True
        return False

    def contains_duplicate_list(self, nums: list[int]) -> bool:
        """
        List
        ----
        Iterate through every element and append to a new list, if
        the element is contained in the new list before the for loop
        is complete, return True, else return False.

        >>> Solution().contains_duplicate_list([1,2,3,1])
        True
        >>> Solution().contains_duplicate_list([1,2,3,4])
        False
        >>> Solution().contains_duplicate_list([1,1,1,3,3,4,3,2,4,2])
        True
        """
        visited = []
        for i in nums:
            if i in visited:
                return True
            else:
                visited.append(i)
        return False

    def contains_duplicate_set(self, nums: list[int]) -> bool:
        """
        Set
        ---
        Create a new set and return False if the length is the same,
        else return True.

        >>> Solution().contains_duplicate_set([1,2,3,1])
        True
        >>> Solution().contains_duplicate_set([1,2,3,4])
        False
        >>> Solution().contains_duplicate_set([1,1,1,3,3,4,3,2,4,2])
        True
        """
        return False if len(set(nums)) == len(nums) else True

    def contains_duplicate_sort(self, nums: list[int]) -> bool:
        """
        Sort
        ----
        Sort the list using built-in sort method for lists, then check
        if the neighbouring elements are equal.

        >>> Solution().contains_duplicate_sort([1,2,3,1])
        True
        >>> Solution().contains_duplicate_sort([1,2,3,4])
        False
        >>> Solution().contains_duplicate_sort([1,1,1,3,3,4,3,2,4,2])
        True
        """
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False
