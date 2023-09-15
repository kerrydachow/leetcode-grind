class Solution:
    """
    Key Takeaways
    -------------
    -   Two pointers to check the widest container
    -   Does not matter how wide, if height is small
    -   Increment smaller height
    -   If height is the same, it does not matter which
        pointer to increment/decrement because subsequent
        volumes are limited by the minimum height
        -   [2, 1000, 1, 2]
        -   6 is most amount of water

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass

    Space Complexity: O(1)
        -   no extra space required
    """
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height)-1
        res = 0
        while i < j:
            max_height = min(height[i], height[j])
            width = j - i
            volume = max_height * width
            res = max(res, volume)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res
