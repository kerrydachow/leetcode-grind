import collections


class Solution:
    """
    Key Takeaways
    -------------
    -   Use a monotonic deque(double-ended queue)
    -   Keep the next largest element's index in line by
        popping tail elements whose value is < new element
    -   When largest element exceeds current window,
        remove from deque => next largest element is waiting
        in line

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   Sliding window: O(n)
        -   popleft(): O(1)
        -   popright(): O(1)

    Space Complexity: O(n)
        -   monotonic deque
    """
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        deque = collections.deque()
        res = []
        l = 0
        for r in range(len(nums)):
            while deque and nums[deque[-1]] < nums[r]:
                deque.pop()
            deque.append(r)
            if r - l + 1 == k:
                res.append(nums[deque[0]])
                l += 1
            if deque[0] < l:
                deque.popleft()
        return res
