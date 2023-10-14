from linked_list import ListNode, Optional

class Solution:
    """
    Key Takeaways
    -------------
    -   Initial solution
    -   2 passes
    -   Dummy node to handle removing first node
    -   Get length
    -   Find the node before nth node
    -   Remove nth node

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   get length: O(n)
        -   remove nth node: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[
        ListNode]:
        # Get Length
        length = 0
        cur = head
        while cur:
            cur, length = cur.next, length + 1

        # Go to the node before nth node
        prev_nth = length - n
        dummy = ListNode(next=head)
        cur = dummy
        for i in range(prev_nth):
            cur = cur.next

        # Remove nth node
        cur.next = cur.next.next
        return dummy.next


class Solution:
    """
    Key Takeaways
    -------------
    -   Use a dummy node to handle removal of the first node
    -   2 nodes: 1 slow, 1 fast
    -   Offset fast node by n
    -   Increment slow and fast until fast is NULL
        -   Slow will be on the node before the nth node
    -   Remove nth node

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = dummy = ListNode(next=head)
        for i in range(n + 1):
            fast = fast.next
        while fast:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return dummy.next
