
class Solution:
    """
    Key Takeaways
    -------------
    -   Sliding window
    -   Count # of chars in t in dictionary
    -   Keep a counter of # chars found of t instead of
        using dictionary to keep count of s's sliding
        window characters
    -   Decrement counter only when the character is
        within the # of characters in t_chars dictionary
        -   e.g. character in t_chars is > 0
    -   When counter == 0, check sliding window length
        with previous minimum
    -   Shift left pointer until counter != 0 while
        continuously checking the window length with
        previous minimum

    Complexity Analysis
    -------------------
    Time Complexity: O(n + m)
        -   create t_chars: O(m)
        -   sliding window: O(n)

    Space Complexity: O(m)
        -   dictionary of count of t's characters: O(m)
    """
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):  # no minimum window substring possible
            return ""
        t_chars = {}
        for char in t:
            t_chars[char] = t_chars.get(char, 0) + 1
        char_count = len(t)
        l, min_l, min_r = 0, 0, len(s)
        for r in range(len(s)):
            if s[r] in t_chars:
                t_chars[s[r]] -= 1
                if t_chars[s[r]] >= 0:
                    char_count -= 1
            while char_count == 0:
                if (r - l + 1) < (min_r - min_l + 1):
                    min_l, min_r = l, r
                if s[l] in t_chars:
                    t_chars[s[l]] += 1
                    if t_chars[s[l]] > 0:
                        char_count += 1
                l += 1
        return s[min_l:min_r + 1] if min_r != len(s) else ""
