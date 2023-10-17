from binary_tree import TreeNode, Optional

class DFS:
    """
    Key Takeaways
    -------------
    -   DFS and swap the values if we're on odd level
    -   Ensure left or right are not NULL
        -   because it is always a perfect tree, we can use OR
    -   Keep track of left node, right node and level in recursive call

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse down the tree: O(n)

    Space Complexity: O(h)
        -   maximum of height # of frames on the tree: O(h)
    """
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root_left, root_right, level):
            if not root_left or not root_right:
                return
            if level % 2 == 1:
                root_left.val, root_right.val = root_right.val, root_left.val
            dfs(root_left.left, root_right.right, level + 1)
            dfs(root_left.right, root_right.left, level + 1)

        dfs(root.left, root.right, 1)
        return root


class BFS:
    """
    Key Takeaways
    -------------
    -   BFS and swap values
    -   Keep track of values of next level
    -   n - i - 1 index will give the opposing index

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse down the tree: O(n)

    Space Complexity: O(w)
        -   maximum of width # of nodes in the queue & values: O(w)
    """
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue, values = [root], []
        level = 0
        while queue:
            next_level, temp = [], []
            n = len(queue)
            for i in range(n):
                node = queue[i]
                if level % 2 == 1:
                    node.val = values[n - i - 1]
                if node.left:
                    next_level.append(node.left)
                    temp.append(node.left.val)
                if node.right:
                    next_level.append(node.right)
                    temp.append(node.right.val)
            values, queue = temp, next_level
            level += 1
        return root
