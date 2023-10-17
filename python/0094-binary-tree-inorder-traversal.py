from binary_tree import TreeNode, Optional

class Iterative:
    """
    Key Takeaways
    -------------
    -   Simulate recursive call stack
    -   Iterate down the left until we hit null
    -   Pop from stack and append that value to res
    -   Reassign root to the right node of the popped node from the stack

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse through the tree: O(n)

    Space Complexity: O(h)
        -   maximum of height # of nodes in the stack: O(h)
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        stack, res = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res


class Recursive:
    """
    Key Takeaways
    -------------
    -   Recursively traverse down the left
    -   Append to result array
    -   Recursively traverse down the right

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse through the tree: O(n)

    Space Complexity: O(h)
        -   maximum of height # of nodes on the call stack: O(h)
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        def traverse(node, arr):
            if not node:
                return
            traverse(node.left, arr)
            arr.append(node.val)
            traverse(node.right, arr)
        res = []
        traverse(root, res)
        return res
