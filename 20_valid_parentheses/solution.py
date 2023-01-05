class Solution:
    """
    20. Valid Parentheses

    Given a string s containing just the characters '(', ')', '{', '}',
    '[' and ']', determine if the input string is valid.

    An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    - Every close bracket has a corresponding open bracket of the same type.
    """
    def isValid(self, s: str) -> bool:
        """
        Stack
        -----
        Using a Stack to store all open brackets and popping the
        bracket out of the stack when the corresponding open bracket
        is in the correct order.

        >>> Solution().isValid("()")
        True
        >>> Solution().isValid("()[]{}")
        True
        >>> Solution().isValid("(]")
        False
        >>> Solution().isValid("{{{}[]}}")
        True
        """
        valid_pairs = {'}': '{', ')': '(', ']': '['}
        stack = []
        for bracket in s:
            # If bracket is a closing bracket
            if bracket in valid_pairs:
                # If stack is not empty & it is a valid pair
                if stack and stack[-1] == valid_pairs[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                # Push every open bracket into the stack
                stack.append(bracket)
        # Check if every parenthesis has been closed
        return True if not stack else False
