import collections


class Solution1:
    """
    Key Takeaways
    -------------
    -   The count of each character is the same for s & t

    Complexity Analysis
    -------------------
    Time Complexity: O(n + m)
        -   n is the # characters in s
        -   m is the # of characters in t

    Space Complexity: O(n + m)
        -   2 counters containing characters of s & t
    """
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)


class Solution2:
    """
    Key Takeaways
    -------------
    -   The count of each character is the same for s & t

    Complexity Analysis
    -------------------
    Time Complexity: O(n + m)
        -   n is the # of characters in s
        -   m is the # of characters in t
        -   because len(s) == len(t), you can say O(n) time complexity

    Space Complexity: O(n + m)
        -   2 counters containing characters of s & t
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            t_count[t[i]] = t_count.get(t[i], 0) + 1

        return s_count == t_count


class Solution3:
    """
    Key Takeaways
    -------------
    -   Built-in all function return True if all iterables return true
    -   26 characters, compare the count of each character in s and t
    -   Built-in functions are optimized

    Complexity Analysis
    -------------------
    Time Complexity: O(26(n + m))
        -   26 characters
        -   count(): O(n) time complexity => on all 26 lowercase chars

    Space Complexity: O(1)
        -   no extra space required
    """
    def isAnagram(self, s: str, t: str) -> bool:
        return all(t.count(x) == s.count(x) for x in
                   "abcdefghijklmnopqrstuvwxyz")
