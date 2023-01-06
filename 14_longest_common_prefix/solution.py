class Solution:
    """
    14. Longest Common Prefix

    Write a function to find the longest common prefix string amongst
    an array of strings.

    If there is no common prefix, return an empty string "".
    """
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        >>> Solution().longestCommonPrefix(["flower","flow","flight"])
        'fl'
        >>> Solution().longestCommonPrefix(["dog","racecar","car"])
        ''
        """
        common_prefix = ""
        for vertical_match_tuple in zip(*strs):
            vertical_match_set = set(vertical_match_tuple)
            if len(vertical_match_set) > 1:
                return common_prefix
            else:
                common_prefix += list(vertical_match_set)[0]
        return common_prefix