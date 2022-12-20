class Solution:
    """
    1. Two Sum

    Given an array of integers nums and an integer target, return indices
    of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you
    may not use the same element twice.

    You can return the answer in any order.
    """
    def two_sum_bf(self, nums: list[int], target: int) -> list[int]:
        """
        Brute Force
        -----------
        Iterate through each element twice and compare the sum to check if the
        sum is equal to the target

        >>> Solution().two_sum_bf([2,7,11,15], 9)
        [0, 1]
        >>> Solution().two_sum_bf([3,2,4], 6)
        [1, 2]
        >>> Solution().two_sum_bf([3,3], 6)
        [0, 1]
        """
        for i_index, i in enumerate(nums):
            for j_index, j in enumerate(nums):
                if i + j == target and i_index != j_index:
                    return [i_index, j_index]

    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """
        Dictionary
        ----------
        Iterate through each element and append (element, index) to dictionary
        or return solution if solution is found.

        >>> Solution().two_sum([2,7,11,15], 9)
        [0, 1]
        >>> Solution().two_sum([3,2,4], 6)
        [1, 2]
        >>> Solution().two_sum([3,3], 6)
        [0, 1]
        """
        visited = {}
        for i_index, i in enumerate(nums):
            difference = target - i
            if difference in visited:
                return [visited.get(difference), i_index]
            if (i, i_index) not in visited.items():
                visited[i] = i_index
