class Solution:
    """
    Key Takeaways
    -------------
    -   Treat the list as a linked list because
        -   The value of each node is between [1, n]
        -   There is only 1 repeat number
    -   Floyd's Cycle Finding Algorithm

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse the list: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                slow = nums[0]
                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]
                return slow
