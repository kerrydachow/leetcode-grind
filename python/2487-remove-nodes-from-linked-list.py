from linked_list import ListNode, Optional

class Solution:
    """
    Key Takeaways
    -------------
    -   Use monotonic stack
        -   pop off the stack of peak.val < curr.val
        -   reassign new peak node's next to curr

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(n)
        -   stack: O(n)
    """
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        stack = [dummy]
        curr = head
        while curr:
            while stack and stack[-1].val < curr.val:
                stack.pop()
                stack[-1].next = curr
            stack.append(curr)
            curr = curr.next
        return dummy.next


class Solution:
    """
    Key Takeaways
    -------------
    -   Reverse linked list
    -   Iterate through reassign curr.next to curr.next.next
        if curr.val > curr.next.val
    -   Reverse linked list again

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   reverse linked list: O(n)
        -   reassigning nodes: O(n)
        -   reverse linked list #2 : O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse list
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Remove nodes
        curr = prev
        while curr:
            while curr.next and curr.val > curr.next.val:
                curr.next = curr.next.next
            curr = curr.next

        # Reverse nodes again
        curr = prev
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


class Solution:
    """
    Key Takeaways
    -------------
    -   Assign head.next to removeNodes(head.next)
    -   Going down the stack check if head < head.next
        -   make sure head.next exists
        -   if true, return head.next
        -   this reassigns head.next to skip this current node

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(n)
        -   n nodes on the call stack: O(n)
    """
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        head.next = self.removeNodes(head.next)
        if head.next and head.val < head.next.val:
            return head.next
        return head
