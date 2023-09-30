class Solution:
    """
    Key Takeaways
    -------------
    -   Monotonic decreasing stack
    -   Store the index of temperature in the stack
    -   Pop when a hotter temperature is occurred
        -   continue to pop and update res
    -   Add new temperature to stack

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   create results array of 0s: O(n)
        -   one pass: O(n)

    Space Complexity: O(n)
        -   stack: O(n)
    """
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                res[stack.pop()] = idx - stack[-1]
            stack.append(idx)
        return res
