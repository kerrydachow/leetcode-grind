from linked_list import ListNode, Optional
class Iterative:
    """
    Key Takeaways
    -------------
    -   Create dummy node at the beginning
    -   Use prev pointer to keep track of previous node
    -   When a node is to be removed no need to reassign prev

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        dum->1->1->1->1->1 val = 1
        """
        dummy = ListNode(next=head)
        curr = head
        prev = dummy
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next


class Recursive:
    """
    Key Takeaways
    -------------
    -   Skip over current node if head.val == val

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(n)
        -   at most n frames on the call stack: O(n)
    """
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head
