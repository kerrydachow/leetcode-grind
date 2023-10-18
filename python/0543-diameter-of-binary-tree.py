from binary_tree import TreeNode, Optional

class Solution:
    """
    Key Takeaways
    -------------
    -   Traverse down the tree with DFS
    -   Keep track of the max diameter using an array (like a global)
    -   At each node, count # of edges to its child on left and right
        -   Add # edges from node's left, and node's right children
        -   This is the diameter of the current node

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse down the tree: O(n)

    Space Complexity: O(h)
        -   maximum of height # of frames on the call stack: O(h)
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            diameter[0] = max(diameter[0], left + right)
            return max(left, right) + 1
        dfs(root)
        return diameter[0]
