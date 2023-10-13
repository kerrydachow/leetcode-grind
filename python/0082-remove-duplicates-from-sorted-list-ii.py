from linked_list import ListNode, Optional

class Solution:
    """
    Key Takeaways
    -------------
    -   Dummy node incase the first node is a duplicate
    -   Keep track of the last unique node
    -   Only reassign the last unique node when you
        know FOR SURE that the new assignment is also unique
    -   Skip all duplicate nodes by checking ahead
    -   Check if unique node's next node == current node
    -   Else reassign unique node's next to current.next
            -   this current node is not unique as we have SKIPPED nodes
            -   reassign to current.next to check skip over this duplicate
                node

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev, curr = dummy, head
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            if prev.next == curr:
                prev = prev.next
            else:
                prev.next = curr.next
            curr = curr.next
        return dummy.next
