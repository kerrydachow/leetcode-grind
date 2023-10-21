from binary_tree import TreeNode, Optional

class Iterative:
    """
    Key Takeaways
    -------------
    -   DFS Preorder traversal iteratively
    -   Append p and q onto stack as tuple
    -   If both nodes exist
        -   If nodes' values differ, return False
        -   Append onto stack
    -   If one node exists but not the other, return False
    -   Return true we finish iterating through while-loop

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse down p: O(n)
        -   traverse down q: O(n)

    Space Complexity: O(h)
        -   maximum of height # of nodes on the stack: O(h)
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            node_p, node_q = stack.pop()
            if node_p and node_q:
                if node_p.val != node_q.val:
                    return False
                stack.append((node_p.left, node_q.left))
                stack.append((node_p.right, node_q.right))
            elif node_p or node_q:
                return False
        return True


class Recursive:
    """
    Key Takeaways
    -------------
    -   If both nodes reach NULL at the same time, return True
    -   If one node doesn't exist or differ in values, return False
    -   Traverse down both trees

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse down p: O(n)
        -   traverse down q: O(n)

    Space Complexity: O(h)
        -   maximum of height # of frames on the call stack: O(h)
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
