from linked_list import ListNode, Optional

class Solution:
    """
    Key Takeaways
    -------------
    -   Use Middle of the Linked List algorithm
    -   Ensure slow pointer is 1 behind the actual
        middle node
    -   Reassign slow.next to slow.next.next

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = dummy = ListNode(next=head)
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return dummy.next
