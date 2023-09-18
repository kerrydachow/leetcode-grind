class Solution:
    """
    Key Takeaways
    -------------
    -   Sliding window problem
    -   Substring is contiguous string in a string
    -   Use a set to handle duplicates because index
        of last duplicate is not important
    -   Once a duplicate is found, increment left pointer
        and remove left pointer character from set
    -   Check the maximum size of window at each iteration

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass
        -   embedded loop increments left pointer
            -   at most O(n)
        -   one pass + incrementing left pointer = O(2n)

    Space Complexity: O(n)
        -   set: O(n)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in found:
                found.remove(s[l])
                l += 1
            res = max(r - l + 1, res)
            found.add(s[r])
        return res
