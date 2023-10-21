from binary_tree import TreeNode, Optional

class Solution:
    """
    Key Takeaways
    -------------
    -   Solve isSameTree
    -   Traverse and find a node equal to subRoot's root
    -   Compare the trees

    Complexity Analysis
    -------------------
    Time Complexity: O(n * m)
        -   traverse down root: O(n)
            -   compare root to subRoot: O(n * m)

    Space Complexity: O(h * k)
        -   where h is the height of root
        -   where k is the height of subRoot
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, a, b):
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)
