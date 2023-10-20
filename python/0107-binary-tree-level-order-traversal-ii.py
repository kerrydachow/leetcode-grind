from binary_tree import TreeNode, Optional
import collections

class BFS:
    """
    Key Takeaways
    -------------
    -   BFS to traverse level by level
    -   Reassign queue to next level of nodes
    -   Reset cur_level_values at each new level
    -   Reverse output

    Complexity Analysis
    -------------------
    Time Complexity: O(n + h)
        -   traverse down the tree: O(n)
        -   Reverse output: O(h)

    Space Complexity: O(w)
        -   maximum of width # of nodes in the queue: O(w)
    """
    def levelOrderBottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root: return []
        queue, res = [root], []
        while queue:
            next_level = []
            cur_level_values = []
            for node in queue:
                cur_level_values.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(cur_level_values)
            queue = next_level
        return res[::-1]


class BFS:
    """
    Key Takeaways
    -------------
    -   BFS to traverse level by level
    -   Use a queue and FIFO operation
    -   Keep track of level
    -   Reverse output

    Complexity Analysis
    -------------------
    Time Complexity: O(n + h)
        -   traverse down the tree: O(n)
        -   Reverse output: O(h)

    Space Complexity: O(w)
        -   maximum of width # of tuples in the queue: O(w)
    """
    def levelOrderBottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root: return []
        queue, res = collections.deque([(root, 0)]), []
        while queue:
            node, level = queue.popleft()
            if node:
                if len(res) <= level:
                    res.append([])
                res[level].append(node.val)
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        return res[::-1]


class DFS:
    """
    Key Takeaways
    -------------
    -   DFS to traverse down the tree
    -   Keep track of the level at each recursive call
    -   Reverse output

    Complexity Analysis
    -------------------
    Time Complexity: O(n + h)
        -   traverse down the tree: O(n)
        -   Reverse output: O(h)

    Space Complexity: O(h)
        -   maximum of height # of frames on the call stack: O(h)
    """
    def levelOrderBottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root: return []
        res = []
        def dfs(root, level):
            if not root:
                return
            if len(res) <= level:
                res.append([])
            res[level].append(root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        dfs(root, 0)
        return res[::-1]
