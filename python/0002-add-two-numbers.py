from linked_list import ListNode, Optional

class Solution:
    """
    Key Takeaways
    -------------
    -   Adding 2 numbers can result in a carry over
    -   Use division with 10 to get the quotient and remainder
        -   quotient is the carry over
        -   remainder is the value of the new node
    -   Handle remaining nodes if one List is smaller than the other

    Complexity Analysis
    -------------------
    Time Complexity: O(n + m)
        -   iterate through l1: O(n)
        -   iterate through l2: O(m)

    Space Complexity: O(1)
        -   no extra space required
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        overflow = 0
        res = dummy = ListNode()
        cur_l1, cur_l2 = l1, l2
        while cur_l1 or cur_l2 or overflow:
            cur_sum = 0
            if cur_l1:
                cur_sum += cur_l1.val
                cur_l1 = cur_l1.next
            if cur_l2:
                cur_sum += cur_l2.val
                cur_l2 = cur_l2.next
            overflow, new_node_val = divmod(cur_sum + overflow, 10)
            dummy.next = ListNode(new_node_val)
            dummy = dummy.next
        return res.next
