from binary_tree import TreeNode

class Iterative:
    """
    Key Takeaways
    -------------
    -   All nodes on left subtree are less than current node
    -   All nodes on right subtree are greater than current node
    -   Check values of p and q compared to root
        -   If root greater, LCA must be on left (lesser)
        -   If root lesser, LCA must be on right (lesser)
        -   Otherwise we are currently at the LCA

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse down the tree: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while True:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root


class Recursive:
    """
    Key Takeaways
    -------------
    -   All nodes on left subtree are less than current node
    -   All nodes on right subtree are greater than current node
    -   If q >= root >= p, this is the LCA
    -   If q <= root <= p, this is the LCA
    -   Otherwise check which side to traverse by comparing
        root to p or q
        -   Traverse left if root is > p or q
        -   Traverse right if root is < p or q

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse down the tree: O(n)

    Space Complexity: O(h)
        -   maximum of height # of frames on call stack: O(h)
    """
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if q.val >= root.val >= p.val or q.val <= root.val <= p.val:
            return root
        if root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return self.lowestCommonAncestor(root.right, p, q)
