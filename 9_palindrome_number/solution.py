class Solution:
    """
    9. Palindrome Number

    Given an integer x, return true if x is a palindrome, and false otherwise.
    """
    def is_palindrome_string(self, x: int) -> bool:
        """
        String
        ------
        Convert int to String and return True or False.

        >>> Solution().is_palindrome_string(121)
        True
        >>> Solution().is_palindrome_string(-121)
        False
        >>> Solution().is_palindrome_string(10)
        False
        """
        x_string = str(x)
        return True if x_string[::-1] == x_string else False

    def is_palindrome(self, x: int) -> bool:
        """
        Modulo
        ------
        Using Modulo to reconstruct reversed number.

        >>> Solution().is_palindrome(121)
        True
        >>> Solution().is_palindrome(-121)
        False
        >>> Solution().is_palindrome(10)
        False
        """
        if x < 0:
            return False
        reverse = 0
        y = x
        while int(y) > 0:
            last_digit = int(y) % 10
            y /= 10
            reverse = (reverse * 10) + last_digit
        return True if reverse == x else False
