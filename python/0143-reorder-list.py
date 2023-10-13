from linked_list import ListNode, Optional

class Solution:
    """
    Key Takeaways
    -------------
    -   Find middle
    -   Reverse middle to end
    -   Reorder the nodes
    -   Must watch out for cycle because last node of the
        first half still points to last node of reversed half
        -   1 -> 2 -> 3 -> 4 -> 5
        -   1 -> 2 -> 3 -> None
        -   5 -> 4 -> 3 -> None
    -   While reordering, make sure tail.next is a valid node
        -   This allows us to skip the reassignment of the
            last node, but still ensures the correct order
        -   1 -> 2 -> 3 -> None | None <- 3 <- 4 <- 5
        -   First iteration
            -   1 -> 5 -> 2 -> 3 -> None  | None <- 3 <- 4
            -   head = 2
            -   tail = 4
        -   Second iteration
            -   1 -> 5 -> 2 -> 4 -> 3 -> None | None <- 3
            -   head = 4
            -   tail = 3
        -   Terminates because tail.next is NULL

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   find middle: O(n)
        -   reverse: O(n)
        -   reorder: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Reorder the nodes
        curr, tail = head, prev
        while tail and tail.next:
            curr_next = curr.next
            tail_next = tail.next

            curr.next = tail
            tail.next = curr_next

            curr = curr_next
            tail = tail_next
