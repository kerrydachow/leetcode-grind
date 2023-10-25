from linked_list import ListNode, Optional

class Solution:
    """
    Key Takeaways
    -------------
    -   Floyd's Cycle Finding Algorithm
    -   Eventually the nodes will meet if there is a cycle
    -   Otherwise if there is no cycle, it will break
        from the loop

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse the linked list: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
