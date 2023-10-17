from binary_tree import TreeNode, Optional

class Iterative:
    """
    Key Takeaways
    -------------
    -   Preorder traversal
        -   Pop off stack and use that node
        -   Check of popped node is not null
    -   Swap the nodes & append left and right to stack

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse down the tree: O(n)

    Space Complexity: O(h)
        -   maximum of height # of nodes on the stack: O(h)
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.right)
                stack.append(node.left)
        return root


class Recursive:
    """
    Key Takeaways
    -------------
    -   Swap left node with right node
    -   Recursively traverse down the tree and return the root
    -   The last return value will be the root node because
        it is the first frame on the call stack
        -   LIFO stack data structure

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse down the tree: O(n)

    Space Complexity: O(h)
        -   maximum of height # of nodes on the call stack: O(h)
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
222222