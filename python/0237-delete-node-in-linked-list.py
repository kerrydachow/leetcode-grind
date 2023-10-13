class Solution:
    """
    Key Takeaways
    -------------
    -   Orphan the neighboring node

    Complexity Analysis
    -------------------
    Time Complexity: O(1)
        -   constant

    Space Complexity: O(1)
        -   constant
    """
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
