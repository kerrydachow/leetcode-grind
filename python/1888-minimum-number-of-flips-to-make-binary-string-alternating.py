class Solution:
    def minFlips(self, s: str) -> int:
        """
        Key Takeaways
        -------------
        -   Add s to s: 111000 + 111000
            -   111000111000
        -   Two possible answers:
            -   010101 or 101010
        -   Extend the two possible answers:
            -   010101010101
            -   101010101010
        -   Sliding window & keep track of
            the # of bits needed to flip

        Complexity Analysis
        -------------------
        Time Complexity: O(n)
            -   s + s: O(n)
            -   create 2 possible answers: O(2n)
            -   Sliding window: O(2n)

        Space Complexity: O(n)
            -   2 possible answers: O(4n)
            -   s + s: O(2n)
        """
        n = len(s)
        s = s + s
        alt_1, alt_2 = "", ""
        for i in range(len(s)):
            alt_1 += "0" if i % 2 else "1"
            alt_2 += "1" if i % 2 else "0"
        res = len(s)
        diff_1, diff_2 = 0, 0
        l = 0
        for r in range(len(s)):
            if s[r] != alt_1[r]:
                diff_1 += 1
            if s[r] != alt_2[r]:
                diff_2 += 1
            if (r - l + 1) > n:
                if s[l] != alt_1[l]:
                    diff_1 -= 1
                if s[l] != alt_2[l]:
                    diff_2 -= 1
                l += 1
            if (r - l + 1) == n:
                res = min(res, diff_1, diff_2)
        return res