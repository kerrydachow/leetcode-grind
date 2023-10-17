from binary_tree import TreeNode, Optional

class Iterative:
    """
    Key Takeaways
    -------------
    -   Append node.val to result as we pop off stack
    -   Append right node before left because of the LIFO
        property of stacks

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse down the tree: O(n)

    Space Complexity: O(h)
        -   maximum of height # of nodes on the stack: O(h)
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        stack, res = [], []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


class Recursive:
    """
    Key Takeaways
    -------------
    -   Recursively traverse down the tree
    -   Add the current node's value to res
    -   Traverse down left
    -   Traverse down right

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse down the tree: O(n)

    Space Complexity: O(h)
        -   maximum of height # of nodes on the stack: O(h)
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        def traverse(root, res):
            if not root:
                return
            res.append(root.val)
            traverse(root.left, res)
            traverse(root.right, res)
        res = []
        traverse(root, res)
        return res
