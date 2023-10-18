from binary_tree import TreeNode, Optional

class Iterative:
    """
    Key Takeaways
    -------------
    -   Preorder traversal
    -   Keep track of the level of the current node
    -   Check if root is NULL before proceeding

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse down the tree: O(n)

    Space Complexity: O(h)
        -   maximum of height # of tuples on the stack: O(h)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        res = 0
        while stack:
            node, level = stack.pop()
            res = max(res, level)
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
        return res


class Recursive:
    """
    Key Takeaways
    -------------
    -   Traverse down the Tree
    -   Get the max of left or right while adding 1 to the current level

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse down the tree: O(n)

    Space Complexity: O(h)
        -   maximum of height # of frames on the call stack: O(h)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
