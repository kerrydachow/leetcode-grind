from linked_list import ListNode, Optional

class Solution:
    """
    Key Takeaways
    -------------
    -   Floyd's Cycle Finding Algorithm
    -   Eventually the nodes will meet if there is a cycle
        -   Once the nodes meet, reset one to the head
        -   Iterate until both nodes are the same

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse the linked list: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
