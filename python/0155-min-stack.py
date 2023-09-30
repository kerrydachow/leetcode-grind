def solution1():
    """
    Key Takeaways
    -------------
    -   Linked list where you reassign the head for every push
    -   Keep track of the min element at every Node
    -   If a node is popped(), the next node on the stack
        will carry the next min node

    Complexity Analysis
    -------------------
    Time Complexity: O(1)
        -   O(1) for all operations

    Space Complexity: O(n)
        -   minimum stack data structure: O(n)
    """
    class MinStack:

        def __init__(self):
            self.element = None

        def push(self, val: int) -> None:
            if not self.element:
                self.element = Node(val, val, None)
            else:
                self.element = Node(val, min(val, self.element.min),
                                    self.element)

        def pop(self) -> None:
            self.element = self.element.next

        def top(self) -> int:
            return self.element.val

        def getMin(self) -> int:
            return self.element.min

    class Node:
        def __init__(self, val: int, min_val: int, next_node):
            self.val = val
            self.min = min_val
            self.next = next_node


def solution2():
    """
    Key Takeaways
    -------------
    -   2 stacks
    -   1 stack to keep track of current value
    -   1 stack to keep track the min value at each iteration
    -   both stacks must always be the same size

    Complexity Analysis
    -------------------
    Time Complexity: O(1)
        -   O(1) for all operations

    Space Complexity: O(n)
        -   2 stacks: O(2n) => O(n)
    """
    class MinStack:

        def __init__(self):
            self.stack = []
            self.min_stack = []

        def push(self, val: int) -> None:
            self.stack.append(val)
            if self.min_stack:
                val = min(self.min_stack[-1], val)
            self.min_stack.append(val)

        def pop(self) -> None:
            self.stack.pop()
            self.min_stack.pop()

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return self.min_stack[-1]
