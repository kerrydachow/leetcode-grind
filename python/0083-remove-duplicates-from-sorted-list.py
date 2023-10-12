from linked_list import ListNode, Optional


class Iterative:
    """
    Key Takeaways
    -------------
    -   Keep track of first instance of a Node
    -   Reassign the first instance's next to a node whose
        value is different
    -   Make sure the first instance of the last
        unique node points to null

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = prev = head
        while curr:
            if curr.val != prev.val:
                prev.next = curr
                prev = curr
            curr = curr.next
        if prev:
            prev.next = None
        return head


class Iterative:
    """
    Key Takeaways
    -------------
    -   Reassign previous to curr.next if their values are the same
    -   Else curr is the first instance of
        a unique value, assign prev to curr

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = prev = head
        while curr and curr.next:
            curr = curr.next
            if prev.val == curr.val:
                prev.next = curr.next
            else:
                prev = curr
        return head


class Recursive:
    """
    Key Takeaways
    -------------
    -   Assign head.next to self.deleteDuplicates(head.next)
    -   As we are popping off the stack
        -   return head.next if head.val == head.next.val to
            skip this current node

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(n)
        -   n frames on the call stack: O(n)
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.next and head.val == head.next.val else head
