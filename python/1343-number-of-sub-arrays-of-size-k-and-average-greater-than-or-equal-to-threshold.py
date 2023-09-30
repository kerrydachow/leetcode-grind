class Solution1:
    """
    Key Takeaways
    -------------
    -   Sliding window
    -   Once length of sliding window == k,
        check the avg with threshold
    -   Subtract left value from current sum, and increment
        left pointer

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass

    Space Complexity: O(1)
        -   no extra space required
    """
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        l = 0
        res = 0
        curr_sum = 0
        for r in range(len(arr)):
            curr_sum += arr[r]
            if r - l + 1 == k:
                res += 1 if curr_sum / k >= threshold else 0
                curr_sum -= arr[l]
                l += 1
        return res


class Solution2:
    """
    Key Takeaways
    -------------
    -   Sliding window
    -   Set curr_sum to values of sliding window
        -   exclude the last value to initialize the
            loop by adding right pointer's value to curr_sum
    -   Check the threshold
    -   Subtract left pointer's value from curr_sum
    -   Increment left pointer

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass

    Space Complexity: O(1)
        -   no extra space required
    """
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        curr_sum = sum(arr[:k - 1])  # exclude last element of window
        res = 0
        l = 0
        for r in range(k - 1, len(arr)):
            curr_sum += arr[r]
            if curr_sum / k >= threshold:
                res += 1
            curr_sum -= arr[l]
            l += 1
        return res
