from linked_list import ListNode, Optional

class Iterative:
    """
    Key Takeaways
    -------------
    -   Initialize new node and begin merging
        -   curr to iterate
        -   dummy to return after merging
    -   Iterate through while both lists are not null
        -   Merge smaller value to curr
        -   Increment the merged list
    -   Assign the rest of the nodes to the tail after loop

    Complexity Analysis
    -------------------
    Time Complexity: O(n + m)
        -   one pass through list1: O(n)
        -   one pass through list2: O(m)

    Space Complexity: O(1)
        -   no extra space required
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        return dummy.next


class Recursive:
    """
    Key Takeaways
    -------------
    -   Base cases to attach the remaining list to the result
    -   After each merge, return the newly merged list
        to the previous call on the call stack

    Complexity Analysis
    -------------------
    Time Complexity: O(n + m)
        -   one pass through list1: O(n)
        -   one pass through list2: O(m)

    Space Complexity: O(n + m)
        -   length of list1 + length of  list2 # of frames
            on the call stack: O(n + m)
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
