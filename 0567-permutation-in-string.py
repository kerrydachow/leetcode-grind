class Solution:
    """
    Key Takeaways
    -------------
    -   Sliding window of length s1
    -   Compare characters of sliding window in O(1) time
        -   Use array of size 26 where each index represents
            a character. e.g. 'a' = arr[0], 'b' = arr[1], ... 'z' = arr[25]

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   Iterate through s1 and s2: O(n)
        -   Compare 2 arrays: O(1)
    Space Complexity: O(52) => O(1)
        -   2 arrays of size 26
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for r in range(len(s1)):
            s1_count[ord(s1[r]) - ord('a')] += 1
            s2_count[ord(s2[r]) - ord('a')] += 1

        if s1_count == s2_count: return True

        l = 0
        for r in range(r + 1, len(s2)):
            s2_count[ord(s2[r]) - ord('a')] += 1
            s2_count[ord(s2[l]) - ord('a')] -= 1
            if s1_count == s2_count: return True
            l += 1
        return False
