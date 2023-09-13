import collections


class Solution1:
    """
    Key Takeaways
    -------------
    - Nested loop brute force

    Complexity Analysis
    -------------------
    Time Complexity: O(n^2)
        -   embedded loop: O(n^2)

    Space Complexity: O(1)
        -   no extra space required
    """
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i_idx, i_num in enumerate(nums):
            for j_idx, j_num in enumerate(nums[i_idx + 1:]):
                if i_num + j_num == target:
                    return [i_idx, j_idx + i_idx + 1]


class Solution2:
    """
    Key Takeaways
    -------------
    -   Dictionary to keep track of visited nums
    -   Duplicate values in dictionary do not matter because the
        algorithm will return before modification is necessary
    -   At each iteration, we can take (target - current_num)
        which is the difference to find
    -   Check the dictionary for the difference
    -   Dictionary operation: if _ in dict: O(1) time complexity

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass
        -   if _ in dict: O(1)
    Space Complexity: O(n)
        -   dictionary containing nums
    """
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visited = {}
        for idx, num in enumerate(nums):
            difference = target - num
            if difference in visited:
                return [visited[difference], idx]
            visited[num] = idx


class Solution3:
    """
    Key Takeaways
    -------------
    -   Sort nums
    -   Make a dict of indices before sorting
     -  Dict contains num as key, and list of indices as value
    -   Set 2 pointers at index 0, len(nums) - 1 respectively
    -   Iterate while left pointer < right pointer<
    -   When sum of pointer 1 and 2 is less than target, increment
        pointer 1
    -   When sum of pointer 1 and 2 is greater than target, decrement
        pointer 2
    -   When returning, check if nums[l] == nums[r]

    Complexity Analysis
    -------------------
    Time Complexity: O(nlogn)
        -   create dictionary of num and its indices: O(n)
        -   sort(): O(nlogn)
        -   two pointer loop: O(n)

    Space Complexity:
        -   dictionary num and its indices: O(n)
    """
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = collections.defaultdict(list)
        for i in range(len(nums)):
            nums_map[nums[i]].append(i)

        nums.sort()

        l, r = 0, len(nums) - 1
        while l < r:
            curr_sum = nums[l] + nums[r]
            if curr_sum > target:
                r -= 1
            elif curr_sum < target:
                l += 1
            else:
                if nums[l] == nums[r]:
                    return [nums_map[nums[l]][0], nums_map[nums[r]][1]]
                return [nums_map[nums[l]][0], nums_map[nums[r]][0]]
