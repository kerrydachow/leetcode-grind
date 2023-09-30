class Solution1:
    """
    Key Takeaways
    -------------
    -   Iterate with two pointers at 0 and len(s)-1
    -   If s[x] != s[y], check if removal of BOTH s[x]
        and s[y] separately, will result in a palindrome
    -   Use helper function to check removals

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass through s
        -   2 instances of character removal for rest of characters
            -   O(2n) worst case

    Space Complexity: O(1)
        -   no extra space required
    """
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.valid_palindrome_helper(s, l, r - 1) or \
                    self.valid_palindrome_helper(s, l + 1, r)
            l += 1
            r -= 1
        return True

    def valid_palindrome_helper(self, s: str, l: int, r: int):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True


class Solution2:
    """
    Key Takeaways
    -------------
    -   Iterate with two pointers at 0 and len(s)-1
    -   If s[x] != s[y], check if removal of BOTH s[x]
        and s[y] separately, will result in a palindrome
    -   Use list slicing and reversing, then compare

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass through s
        -   reverse with list slicing: O(n)

    Space Complexity: O(n)
        -   2 slices of both possibly removals: O(2n)
    """
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                l_removal = s[l + 1:r + 1]
                r_removal = s[l:r]
                return l_removal == l_removal[::-1] or r_removal == \
                    r_removal[::-1]
        return True
