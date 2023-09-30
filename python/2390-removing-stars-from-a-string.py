class Solution1:
    """
    Key Takeaways
    -------------
    -   Stack
    -   Append to stack if not *
    -   If * pop from stack

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)
        -   stack.append(): O(1)
        -   stack.pop(): O(1)

    Space Complexity: O(n)
        -   stack: O(n)
    """
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
