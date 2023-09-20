class Solution:
    """
    Key Takeaways
    -------------
    -   Sliding window
    -   Maintain length k
    -   Track the # of vowels in window of length k

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   sliding window: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        l = 0
        vowel_count = 0
        res = 0
        for r in range(len(s)):
            if s[r] in vowels:
                vowel_count += 1
            if r - l + 1 == k:
                res = max(res, vowel_count)
                vowel_count -= 1 if s[l] in vowels else 0
                l += 1
        return res
