class Solution1:
    """
    Key Takeaways
    -------------
    -   Simulation
    -   Simulate using a stack and performing the
        push and pop operations to assess feasibility
    -   Peek and check if top of stack == popped[p]

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass

    Space Complexity: O(n)
        -   stack: O(n)
        -   res: O(n)
    """
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        res = []
        popped_pointer = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[popped_pointer]:
                res.append(stack.pop())
                popped_pointer += 1
        return res == popped


class Solution2:
    """
    Key Takeaways
    -------------
    -   Stack
    -   Optimized space complexity from first solution
    -   Same idea, but concise code

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(n)
        -   stack: O(n)
    """
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        j = 0
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return len(stack) == 0


class Solution3:
    """
    Key Takeaways
    -------------
    -   Use pushed as stack
    -   Assign the i'th element as the current iteration in pushed
    -   Increment i, so it represents the SIZE of the stack
        -   simulating appending to the stack
    -   When pushed[i-1] == popped[j] decrement i pointer
        -   simulating popping off the stack
    -   Modifies the input which is generally bad practice

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(1)
        -   Modified space: O(n)
        -   Extra space: O(1)
    """
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        i = 0
        j = 0
        for num in pushed:
            pushed[i] = num
            i += 1
            while i > 0 and pushed[i - 1] == popped[j]:
                i -= 1
                j += 1
        return i == 0
