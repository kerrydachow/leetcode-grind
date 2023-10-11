from linked_list import ListNode, Optional

class Solution:
    """
    Key Takeaways
    -------------
    -   Fast and slow pointer
    -   Slow pointer will end up in trailing middle

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow