class Solution:
    """
    Key Takeaways
    -------------
    -   Stack to store parentheses
    -   Backtrack to generate all combinations
    -   Pop after each backtrack call
    -   Append to result when length of stack == n

    Complexity Analysis
    -------------------
    Time Complexity: O(4^n)
        -   recursive tree height: 2n, therefore
            -   max nodes in tree: O(2^2n)

    Space Complexity: O(n)
        -   height of 2n at most: O(2n) => O(n)
    """
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(open_n, closed_n):
            if open_n == closed_n == n:
                res.append("".join(stack))
                return
            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, closed_n)
                stack.pop()
            if closed_n < open_n:
                stack.append(")")
                backtrack(open_n, closed_n + 1)
                stack.pop()

        backtrack(0, 0)
        return res
