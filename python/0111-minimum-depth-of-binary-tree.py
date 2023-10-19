from binary_tree import TreeNode, Optional
import collections

class DFS:
    """
    Key Takeaways
    -------------
    -   If the left or right node from the root does not exist,
        we can take the depth of whichever exists
    -   If the left and right node exists from the root, we can
        take the min of the 2 depths

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -    traverse down the tree: O(n)

    Space Complexity: O(h)
        -   maximum of height # of frames on the call stack: O(h)
    """
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

class BFS:
    """
    Key Takeaways
    -------------
    -   BFS until we hit a leaf node
    -   Keep track of the depth using a tuple of the node and depth
    -   Return the depth of the leaf node

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse down the tree: O(n)

    Space Complexity: O(w)
        -   maximum of width # of tuples in the queue: O(w)
    """
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return depth
                else:
                    queue.append((node.left, depth + 1))
                    queue.append((node.right, depth + 1))
