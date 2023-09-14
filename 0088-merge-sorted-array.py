class Solution1:
    """
    Key Takeaways
    -------------
    -   Modify in-place from the last index to the first index
    -   Greatest -> smallest

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass

    Space Complexity: O(1)
        -   no extra space required
    """
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in range(len(nums1) -1, -1, -1):
            if m > 0 and n > 0:
                if nums1[m - 1] > nums2[n - 1]:
                    nums1[i] = nums1[m - 1]
                    m -= 1
                else:
                    nums1[i] = nums2[n - 1]
                    n -= 1
            elif n > 0:
                nums1[i] = nums2[n - 1]
                n -= 1
            else:
                return nums1


class Solution2:
    """
    Key Takeaways
    -------------
    -   n + m - 1 will be the index
    -   if n > 0 merge the remaining into nums1

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass

    Space Complexity: O(1)
        -   no extra space required
    """
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
