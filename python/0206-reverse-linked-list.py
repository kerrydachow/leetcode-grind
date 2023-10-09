from linked_list import ListNode, Optional

class Iterative:
    """
    Key Takeaways
    -------------
    -   Keep track of previous node
    -   Keep track of the next node at current iteration
    -   Reassign next node to previous
    -   Reassign previous to current node
    -   Assign current node to next node
    -   Return previous node because curr will be None at
        the last iteration

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


class Recursive:
    """
    Key Takeaways
    -------------
    -   Recursively iterate until the last node
        -   Check if head.next is null
    -   Assign last node to a variable
    -   Go down the call stack (popping off the stack)
    -   Recursive sub-problem: [4 -> 5 -> None]
        -   At this iteration, head points to 4
        -   Assign 5 to point to 4: [4 -> <- 5 <- None]
        -   Assign 4 to point to a NEW None: [None <- 4 <- 5 <- None]
    -   Continue down the stack
    -   Return last node

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(n)
        -   n frames on the call stack: O(n)
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
