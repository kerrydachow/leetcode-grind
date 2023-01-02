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

    def contains_duplicate_dictionary(self, nums: list[int]) -> bool:
        """
        Dictionary
        ----------
        Iterate through every element and append to a new dict, if
        the element is contained in the new duct before the for loop
        is complete, return True, else return False.

        Dictionary "x in d" operation has an average time complexity of
        O(1) and a worse case of O(n).

        List "x in l" operation has an average time complexity of O(n).

        Therefore, a dictionary is more efficent when finding duplicates
        of a large list.

        >>> Solution().contains_duplicate_dictionary([1,2,3,1])
        True
        >>> Solution().contains_duplicate_dictionary([1,2,3,4])
        False
        >>> Solution().contains_duplicate_dictionary([1,1,1,3,3,4,3,2,4,2])
        True
        """
        visited = {}
        for i in nums:
            if i in visited:
                return True
            else:
                visited[i] = 1
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
