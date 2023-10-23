from binary_tree import TreeNode, Optional

class Solution:
    """
    Key Takeaways
    -------------
    -   Take the middle node
    -   Create new node with middle
        -   DFS [lo: mid-1] for left child
        -   DFS [mid+1: hi] for right child

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   traverse through every node

    Space Complexity: O(logn)
        -   maximum of logn # of frames on call stack: O(logn)
    """
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def dfs(lo, hi):
            if lo > hi:
                return
            mid = lo + (hi - lo) // 2
            return TreeNode(nums[mid], dfs(lo, mid - 1), dfs(mid + 1, hi))
        return dfs(0, len(nums) - 1)
