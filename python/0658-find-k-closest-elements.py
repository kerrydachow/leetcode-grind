class Solution1:
    """
    Key Takeaways
    -------------
    -   Binary search to find x or closest element to x
        -   lower bound binary search
        -   compare lower bound to next element and
            check "a is closer to b" conditions
    -   Sliding window
        -   ensure look_left and look_right are between bounds

    Complexity Analysis
    -------------------
    Time Complexity: O(logn + k)
        -   binary search: O(logn)
        -   sliding window: O(k)

    Space Complexity: O(1)
        -   no extra space required
    """
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        l = r = self.binary_search(arr, x)
        while r - l + 1 < k:
            look_left = l - 1
            look_right = r + 1
            if look_left > -1 and look_right < len(arr):
                if abs(arr[look_left] - x) <= abs(arr[look_right] - x):
                    l -= 1
                else:
                    r += 1
            elif look_left < 0:
                r += 1
            else:
                l -= 1
        return arr[l:r + 1]

    def binary_search(self, nums, target):
        """
        Binary search to find lower bound if target does not exist.
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid
        return lo if lo + 1 >= len(nums) or abs(nums[lo] - target) <= abs(
            nums[lo + 1] - target) else lo + 1


class Solution2:
    """
    Key Takeaways
    -------------
    -   Not very intuitive
    -   Binary search to find the best possible sliding window
        -   find the start value of the sliding window
        -   x - arr[mid] > arr[mid + k] - x:
            -   Checking if current mid is a better candidate
                than mid + k
            -   Why x - arr[mid] and not abs(x - arr[mid])???
                -   the math just works out...

    Complexity Analysis
    -------------------
    Time Complexity: O(logn - k)
        -   binary search on n-k elements: O(logn-k)

    Space Complexity: O(1)
        -   no extra space required
    """
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        lo, hi = 0, len(arr) - k
        while lo < hi:
            mid = (lo + hi) // 2
            if x - arr[mid] > arr[mid + k] - x:
                lo = mid + 1
            else:
                hi = mid
        return arr[lo: lo + k]
