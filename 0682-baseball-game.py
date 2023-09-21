class Solution:
    """
    Key Takeaways
    -------------
    -   Use stack to remove items & peek

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)
        -   stack peek: O(1)
        -   pop(): O(1)

    Space Complexity: O(n)
        -   stack: O(n)
    """
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(op))
        return sum(stack)
