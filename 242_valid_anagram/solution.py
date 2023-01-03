class Solution:
    """
    242. Valid Anagram

    Given two strings s and t, return true if t is an anagram of s,
    and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters
    of a different word or phrase, typically using all the original
    letters exactly once.
    """

    def isAnagram_bf(self, s: str, t: str) -> bool:
        """
        >>> Solution().isAnagram_bf("anagram", "nagaram")
        True
        >>> Solution().isAnagram_bf("rat", "car")
        False
        """
        if len(s) != len(t):
            return False
        char_t = list(t)
        for x in s:
            if x in char_t:
                char_t.remove(x)
        return True if len(char_t) == 0 else False

    def isAnagram_dict(self, s: str, t:str) -> bool:
        """
        >>> Solution().isAnagram_dict("anagram", "nagaram")
        True
        >>> Solution().isAnagram_dict("rat", "car")
        False
        """
        count_s, count_t = {}, {}
        for char_s in s:
            if char_s not in count_s:
                count_s[char_s] = 1
            else:
                count_s[char_s] += 1
        for char_t in t:
            if char_t not in count_t:
                count_t[char_t] = 1
            else:
                count_t[char_t] += 1
        return count_s.items() == count_t.items()

    def isAnagram_counter(self, s: str, t: str) -> bool:
        """
        >>> Solution().isAnagram_counter("anagram", "nagaram")
        True
        >>> Solution().isAnagram_counter("rat", "car")
        False
        """
        from collections import Counter
        return Counter(s).items() == Counter(t).items()

    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check the count of all characters of s and t using Python
        Generator Expressions and the all() function.

        >>> Solution().isAnagram("anagram", "nagaram")
        True
        >>> Solution().isAnagram("rat", "car")
        False
        """
        return all(s.count(x) == t.count(x) for x in 'abcdefghijklmnopqrstuvwxzy')
