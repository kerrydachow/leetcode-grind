from linked_list import ListNode, Optional

class Solution:
    """
    Key Takeaways
    -------------
    -   Use 2 stacks to maintain reverse order
    -   Pop off stack and use divmod
    -   Create the linked list from reverse
        -   Reassign the head at each new node

    Complexity Analysis
    -------------------
    Time Complexity: O(n + m)
        -   create stack1: O(n)
        -   create stack2: O(m)
        -   iterate through stacks: O(n || m)

    Space Complexity: O(n + m)
        -   stack1: O(n)
        -   stack2: O(m)
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        overflow = 0
        dummy = None

        while stack1 or stack2 or overflow:
            cur_sum = 0
            if stack1:
                cur_sum += stack1.pop()
            if stack2:
                cur_sum += stack2.pop()
            overflow, cur_node_val = divmod(cur_sum + overflow, 10)
            cur_node = ListNode(cur_node_val, dummy)
            dummy = cur_node
        return dummy
