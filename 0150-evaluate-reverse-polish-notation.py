class Solution:
    """
    Key Takeaways
    -------------
    -   Stack
    -   Append into stack after evaluating expression
    -   Truncate towards 0 => int(a / b)

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)
        -   if _ in set: O(1)
        -   stack.pop(): O(n)

    Space Complexity: O(n)
        -   stack: O(n)
        -   set: O(4)
    """
    def evalRPN(self, tokens: list[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == "+":
                    result = operand1 + operand2
                elif token == "-":
                    result = operand1 - operand2
                elif token == "*":
                    result = operand1 * operand2
                elif token == "/":
                    result = int(operand1 / operand2)
                stack.append(result)
        return stack[0]
