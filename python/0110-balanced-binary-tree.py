from binary_tree import TreeNode, Optional

class DFS:
    """
    Key Takeaways
    -------------
    -   Get the depth of every subtree
    -   Check if the difference between 2 subtrees
        are greater than 1
    -   Iterate down the tree

    Complexity Analysis
    -------------------
    Time Complexity: O(n^2)
        -   traverse down the tree: O(n)
            -   get the depth of each subtree: O(n)

    Space Complexity: O(h)
        -   getDepth: O(h)
        -   traverse down the tree: O(h)
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if abs(self.getDepth(root.left) - self.getDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getDepth(self, root):
        if not root:
            return 0
        return max(self.getDepth(root.left), self.getDepth(root.right)) + 1

class DFS:
    """
    Key Takeaways
    -------------
    -   Bottom-up DFS approach
    -   Traverse down the tree and get the depths
    -   Check difference in depths
        -   If difference is > 1, return -1
        -   Carry the -1 to the root

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse down the tree: O(n)

    Space Complexity: O(h)
        -   height # of frames on the call stack: O(h)
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return dfs(root) != -1
