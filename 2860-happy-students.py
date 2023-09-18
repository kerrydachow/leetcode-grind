class Solution:
    """
    Key Takeaways
    -------------
    -   Sort nums
    -   Check if the first element is > 0
        -   This means the teacher is able to select no students to form
            groups
    -   Iterate from largest -> smallest (reversed)
        -   Keep track of previous value
        -   Assume all students are selected
    -   Check if current # of selected students > current value
    -   Check if previous students who are deselected values
        are > # of selected students
        -   because the list is sorted, if the prev value dissatisfies
            the condition, then all lather students who were deselected
            are also not happy

    Complexity Analysis
    -------------------
    Time Complexity: O(nlogn)
        -   sort: O(nlogn)

    Space Complexity: O(1)
        -   no extra space required
    """
    def countWays(self, nums: list[int]) -> int:
        nums.sort()
        res = 0
        prev = float("inf")

        # Select None
        if nums[0] > 0:
            res += 1

        # Selected students
        for i in range(len(nums) - 1, -1, -1):
            selected = i + 1

            # 1st condition: Total # selected students > nums[i]
            # 2nd condition: All non-selected students value are > # of selected students
            if selected > nums[i] and prev > selected:
                res += 1
            prev = nums[i]
        return res
