class Solution:
    """
    Key Takeaways
    -------------
    -   XORing 2 identical numbers returns 0
    -   Iterate through and XOR all values against
        each other
    -   Remaining value will be the single number

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
