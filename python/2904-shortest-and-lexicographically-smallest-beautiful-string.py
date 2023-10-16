class Solution:
    """
    Key Takeaways
    -------------
    -   Sliding window
    -   If the window is the same length
        -   Use XOR to determine which is lexicographically smaller
        -   e.g.
            -   k = 4
            -   window_a = 11101, window_b = 11011
            -   window_a ^ 11111 = 00010
            -   window_b ^ 11111 = 00100
            -   00100 > 00010therefore window_b is lexicographically smaller than window_a

    Complexity Analysis
    -------------------
    Time Complexity: O(n^2)
        -   Sliding Window: O(n)
            -   Casting str to int: O(n)

    Space Complexity: O(n)
        -   Slicing s: O(n)
    """
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        min_l, min_r = 0, len(s)
        l, ones = 0, 0
        for r in range(len(s)):
            if s[r] == "1":
                ones += 1
            while ones == k:
                if min_r - min_l + 1 == r - l + 1:
                    a = int(s[min_l: min_r + 1], 2)
                    b = int(s[l: r + 1], 2)
                    c = int("1" * (r - l + 1), 2)
                    if b ^ c > a ^ c:
                        min_l, min_r = l, r
                elif r - l + 1 < min_r - min_l + 1:
                    min_l, min_r = l, r
                if s[l] == "1":
                    ones -= 1
                l += 1
        return "" if min_r == len(s) else s[min_l: min_r + 1]
