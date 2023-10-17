from binary_tree import TreeNode, Optional

class Solution:
    """
    Key Takeaways
    -------------
    -   Simulate recursive call stack
    -   Must keep track of visited nodes
    -   If node has been visited, append into result array
    -   Else if node has not been visited and node exists
        -   Append node onto stack, append True to visited
        -   Append node.right onto stack and False to visited
        -   Append node.left onto stack and False to visited

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse down the tree

    Space Complexity: O(h)
        -   maximum of height # of noes on the stack and visited: O(h)
    """
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res, stack, visited = [], [root], [False]
        while stack:
            node, v = stack.pop(), visited.pop()
            if v:
                res.append(node.val)
            elif node:
                stack.append(node)
                visited.append(True)
                stack.append(node.right)
                visited.append(False)
                stack.append(node.left)
                visited.append(False)
        return res


class Solution:
    """
    Key Takeaways
    -------------
    -   Recursively traverse down the tree
    -   Traverse down the left
    -   Traverse down the right
    -   Add the current node's value into res

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse down the tree: O(n)

    Space Complexity: O(h)
        -   maximum height # of nodes on the call stack: O(H)
    """
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        def traverse(root, res):
            if not root:
                return
            traverse(root.left, res)
            traverse(root.right, res)
            res.append(root.val)
        res = []
        traverse(root, res)
        return res
