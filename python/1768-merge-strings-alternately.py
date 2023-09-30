class Solution:
    """
    Key Takeaways
    -------------
    -   Ensure not out of bounds

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)
        -   "".join(): O(n)

    Space Complexity: O(n)
        -   merged array: O(n)
    """
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        larger_word = max(len(word1), len(word2))
        for i in range(larger_word):
            if i < len(word1):
                merged.append(word1[i])
            if i < len(word2):
                merged.append(word2[i])
        return "".join(merged)
