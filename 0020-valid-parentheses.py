class Solution:
    """
    Key Takeaways
    -------------
    -   First in last out => stack
    -   Stack to keep track of open brackets
    -   If closing bracket doesn't match last open
        bracket in stack => invalid parentheses
    -   If closing parentheses but stack is
        empty => invalid parentheses
    -   Check if stack is empty

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(n)
        -   bracket dictionary: O(3)
        -   stack: O(n)
    """
    def isValid(self, s: str) -> bool:
        valid_pairs = {'{': '}', '(': ')', '[': ']'}
        stack = []
        for bracket in s:
            if bracket in valid_pairs:
                stack.append(bracket)
            elif not stack or valid_pairs[stack.pop()] != bracket:
                return False
        return False if stack else True
