class Solution1:
    """
    Key Takeaways
    -------------
    -   Keep track of count of characters using dictionary
    -   Sliding window of previous longest repeating characters' length
    -   Find out how many characters to replace at each iteration
        -   compare to k
        -   if > k, move left pointer

    Complexity Analysis
    -------------------
    Time Complexity: O(26n)
        -   max(count.values()): O(26)
        -   iterate through s: O(n)

    Space Complexity: O(26)
        -   maximum of 26 characters in dictionary
    """
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


class Solution2:
    """
    Key Takeaways
    -------------
    -   Same solution as above but optimized
    -   Keep track of the current most frequent character
    -   Even if we shift the left pointer, it won't affect the
        maximum most frequent character
    -   The maximum most frequent character will be the result
        unless it has been surpassed
    -   Still decrement left pointer character from dictionary
        to avoid inflated counts of characters for current
        sliding window

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)
        -   while loop to increment left pointer: O(n)

    Space Complexity: O(26)
        -   maximum of 26 characters in dictionary
    """
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        max_f = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_f = max(max_f, count[s[r]])
            while (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
