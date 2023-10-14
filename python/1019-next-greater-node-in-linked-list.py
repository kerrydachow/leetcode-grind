from linked_list import ListNode, Optional

class Solution:
    """
    Key Takeaways
    -------------
    -   Monotonic decreasing stack
        -   Store index and value of last node
    -   Use length of res to determine index

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass through head: O(n)
        -   while-loop pop off stack: O(n)

    Space Complexity: O(n)
        -   stack: O(n)
    """
    def nextLargerNodes(self, head: Optional[ListNode]) -> list[int]:
        res, stack, cur = [], [], head
        while cur:
            while stack and stack[-1][1] < cur.val:
                res[stack.pop()[0]] = cur.val
            stack.append((len(res), cur.val))
            res.append(0)
            cur = cur.next
        return res
