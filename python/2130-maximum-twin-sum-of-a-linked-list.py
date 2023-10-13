from linked_list import ListNode, Optional

class Solution:
    """
    Key Takeaways
    -------------
    -   Naive solution
    -   Create an array of the values
    -   2-pointers to find maximum twin sum

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   create values array: O(n)
        -   two pointer loop: O(n)

    Space Complexity: O(n)
        -   values array: O(n)
    """
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        res = 0
        i, j = 0, len(values) - 1
        while i < j:
            res = max(res, values[i] + values[j])
            i += 1
            j -= 1
        return res


class Solution:
    """
    Key Takeaways
    -------------
    -   Find middle
    -   Reverse middle to end
    -   Iterate through head and tail
        -   Compare values to find maximum twin sum
    -   Input is guaranteed to have an even # of nodes

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   find mid: O(n)
        -   reverse latter mid: O(n)
        -   compare values: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find mid
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse latter half
        prev = None
        cur = slow
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        # Compare
        res = 0
        cur, tail = head, prev
        while tail:
            res = max(res, cur.val + tail.val)
            cur = cur.next
            tail = tail.next
        return res
