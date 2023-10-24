from binary_tree import TreeNode, Optional

class Recursive:
    """
    Key Takeaways
    -------------
    -   Traverse down the tree
    -   Check if it is a leaf node
        -   Subtract current node from targetSum and return True if 0
    -   Traverse left & right, subtract root.val from targetSum
    -   Only one leaf needs to be True to return True

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse down the tree: O(n)

    Space Complexity: O(h)
        -   maximum of height # of frames on call stack: O(h)
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return (targetSum - root.val) == 0
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

class Iterative:
    """
    Key Takeaways
    -------------
    -   Use a stack to simulate call stack
        -   Keep track of node & current sum
    -   If current node has no left nor right node, it is a leaf node
        -   Check if the sum == targetSum
    -   Return False once stack is empty

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse down the tree: O(n)

    Space Complexity: O(h)
        -   maximum of height # of tuples on stack: O(h)
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, curSum = stack.pop()
            if not node.left and not node.right and curSum == targetSum:
                return True
            if node.left:
                stack.append((node.left, node.left.val + curSum))
            if node.right:
                stack.append((node.right, node.right.val + curSum))
        return False
