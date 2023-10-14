from linked_list import ListNode, Optional

class Solution:
    """
    Key Takeaways
    -------------
    -   Swap values not the nodes pointers
    -   Find kth node from the beginning
    -   Use that offset and find the kth node from the end
    -   Perform swap

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = right = head
        for i in range(1, k):
            left = left.next

        fast = left
        while fast.next:
            right = right.next
            fast = fast.next

        left.val, right.val = right.val, left.val
        return head


class Solution:
    """
    Key Takeaways
    -------------
    -   Use a dummy node to handle swaps at the beginning of the list
    -   Swap the node's pointers
    -   Use a pre_left and pre_right pointer to keep track of the
        nodes before kth from the beginning and kth from end
            -   start them at dummy node
    -   Find kth node from the beginning
    -   Use that offset and find kth node from the end
    -   Swap pre_right and pre_left next nodes
    -   Swap left and right next nodes
    -   Return dummy.next

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[
        ListNode]:
        dummy = ListNode(next=head)
        pre_left = pre_right = dummy
        left = right = head

        for i in range(1, k):
            pre_left = pre_left.next
            left = left.next

        fast = left
        while fast.next:
            pre_right = pre_right.next
            right = right.next
            fast = fast.next

        pre_right.next, pre_left.next = left, right
        left.next, right.next = right.next, left.next
        return dummy.next
