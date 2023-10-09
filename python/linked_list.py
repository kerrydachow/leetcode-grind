from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        values = []
        node = self
        while node:
            values.append(node.val)
            node = node.next
        return str(values)

def list_to_link(arr):
    curr = dummy = ListNode(0)
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next
