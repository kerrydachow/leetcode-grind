from linked_list import ListNode, Optional

class Solution:
    """
    Key Takeaways
    -------------
    -   In-place swap
    -   Keep track of the even's head
    -   Keep track of odd's tail
    -   Allow curr to always be even
    -   Check if there is a curr.next
        -   this ensures there will be an odd node to swap

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr, even_head, odd_tail = head.next, head.next, head
        while curr and curr.next:  # curr will always be an even node
            odd_tail.next = curr.next  # reassign odd_tail to curr.next
            odd_tail = odd_tail.next  # reassign odd_tail to the new tail
            curr.next = odd_tail.next  # reassign curr node to point to the newly assigned odd_tail's next node
            odd_tail.next = even_head  # reassign newly assigned odd_tail.next to the beginning of the even_nodes
            curr = curr.next  # next node will be even
        return head


class Solution:
    """
    Key Takeaways
    -------------
    -   Build odd & even list separate
    -   Connect odd's tail to even's head

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        even_head = head.next
        p1, p2 = head, head.next
        while p1.next and p2.next:
            p1.next, p2.next = p2.next, p2.next.next
            p1, p2 = p1.next, p2.next
        p1.next = even_head
        return head
