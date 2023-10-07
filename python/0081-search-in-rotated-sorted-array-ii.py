class Solution:
    """
    Key Takeaways
    -------------
    -   Same solution as Search In Rotated Sorted Array but
        -   Decrement hi if nums[mid] == nums[hi]
        -   When this is the case, we do not know which
            part of the array to slice
        -   Therefore as we decrease hi, we're searching
            both the lo portion and hi portion to find
            the target
            -   mid = hi + lo // 2

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   avg: O(logn) when binary searching
        -   worst case: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def search(self, nums: list[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[hi]:  # the trick
                hi -= 1
            elif nums[mid] > nums[hi]:
                if nums[mid] > target >= nums[lo]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False
