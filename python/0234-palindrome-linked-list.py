from linked_list import ListNode, Optional

class Solution:
    """
    Key Takeaways
    -------------
    -   Find middle with slow & fast pointer
    -   Reverse linked list from middle
    -   Compare head and tail to check if palindrome
    -   curr's last node will point to tail of reverse_curr
        head =          1 -> 2 -> 3 -> 2 -> 1
        curr =          1 -> 2 -> 3 -> None
        reverse_curr =  1 -> 2 -> 3 -> None

        head =          1 -> 2 -> 2-> 1
        curr =          1 -> 2 -> 2 -> None
        reverse_curr =  1 -> 2 -> None

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   iterate to find middle: O(n)
        -   reverse middle: O(n)
        -   compare middle: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find the middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse List from Middle
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Compare head and tail
        curr = head
        reverse_curr = prev
        while reverse_curr:
            if reverse_curr.val != curr.val:
                return False
            reverse_curr = reverse_curr.next
            curr = curr.next
        return True
