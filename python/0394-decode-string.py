class Solution:
    """
    Key Takeaways
    -------------
    -   Stack to store previous char
    -   When closed ] is found, create pattern
    -   Join stack at the end

    Complexity Analysis
    -------------------
    Time Complexity: O(n + k * m)
        -   one pass: O(n)
            -   pop until [: O(n)
            -   pop until num is found: O(n)
            -   .join and reverse: O(j)
                -   where j is length of num
            -   num * str: O(k * m)
                -   where k is num
                -   where m is length of pattern

    Space Complexity: O(n + m * k)
        -   stack: O(n)
        -   repeated pattern: O(m * k)
        -   repeat array: O(3)
        -   pattern: O(n)
    """
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "]":
                pattern = []
                while stack[-1] != "[":  # O(n)
                    pattern.append(stack.pop())
                stack.pop()
                repeat = []
                while stack and stack[-1].isdigit():  # O(n)
                    repeat.append(stack.pop())
                repeat = int("".join(repeat[::-1]))
                pattern = "".join(reversed(pattern))
                stack.append(repeat * pattern)  # O(k*m)
            else:
                stack.append(c)
        return "".join(stack)


class Solution:
    """
    Key Takeaways
    -------------
    -   Build pattern from left to right
    -   Use stack to maintain previous built strings
    -   Add pattern to stack when a [ is met
    -   Decode and multiply when ] is met
    -   Can build count by * by 10 because we are
        building from left -> right

    Complexity Analysis
    -------------------
    Time Complexity: O(n + k * m)
        -   one pass: O(n)
        -   num * str: O(k * m)
            -   where k is the num
            -   where m is the length of pattern

    Space Complexity: O(n + k * m)
        -   stack: O(n)
        -   repeated pattern: O(k * m)
    """
    def decodeString(self, s: str) -> str:
        stack = []
        pattern = ""
        count = 0
        for c in s:
            if c == "[":
                stack.append(pattern)
                stack.append(count)
                pattern = ""
                count = 0
            elif c == "]":
                repeat = stack.pop()
                prefix = stack.pop()
                pattern = prefix + (repeat * pattern)
            elif c.isdigit():
                count *= 10
                count += int(c)
            else:
                pattern += c
        return pattern
