class Solution1:
    """
    Key Takeaways
    -------------
    -   Set to store found numbers
    -   Two pointers
    -   Keep sliding window of size k
    -   If duplicate is found within the window, return True

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass

    Space Complexity: O(n)
        -   set to store found numbers: O(n)
    """
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        found = set([nums[0]])
        l = 0
        for r in range(1, len(nums)):
            if r - l > k:
                found.remove(nums[l])
                l += 1
            if nums[r] in found:
                return True
            found.add(nums[r])
        return False


class Solution2:
    """
    Key Takeaways
    -------------
    -   Dictionary to keep track of visited & its index
    -   Check if num has been visited
    -   Check if difference of indices are <= k

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass

    Space Complexity: O(n)
        -   dictionary storing visited: O(n)
    """

    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        visited = {}
        for idx, num in enumerate(nums):
            if num in visited and idx - visited[num] <= k:
                return True
            visited[num] = idx
        return False
