from linked_list import ListNode, Optional

class Solution:
    """
    Key Takeaways
    -------------
    -   Combine both linked lists and iterate through
    -   When both linked lists point to the same Node
        or None, the loop will break

    Complexity Analysis
    -------------------
    Time Complexity: O(n + m)
        -   iterating through a and b combined: O(n + m)

    Space Complexity: O(1)
        -   no extra space required
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
