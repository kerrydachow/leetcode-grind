class Solution1:
    """
    Key Takeaways
    -------------
    -   Use an extra array
    -   Partition nums and append to extra array
    -   Loop through nums and reassign each element in-place to output

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   Loop through first partition: O(k)
        -   Loop through second partition: O(n - k)
        -   Loop through nums to reassign: O(n)

    Space Complexity: O(n)
        -   extra array to reassign
    """
    def rotate(self, nums: list[int], k: int) -> None:
        rotations = k % len(nums)
        output = []

        for i in range(len(nums) - rotations, len(nums)):
            output.append(nums[i])

        for i in range(len(nums) - rotations):
            output.append(nums[i])

        for i in range(len(nums)):
            nums[i] = output[i]


class Solution2:
    """
    Key Takeaways
    -------------
    -   Similar to above but optimized
    -   Offset the index of extra array to rotated index
        -   use % to ensure loops around to the 2nd partition

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   create output array: O(n)
        -   reassign nums: O(n)

    Space Complexity: O(n)
        -   extra array to reassign
    """
    def rotate(self, nums: list[int], k: int) -> None:
        size = len(nums)
        rotations = k % size

        if rotations == 0:
            return

        output = [0] * size

        for i in range(size):
            offset = (i + k) % size
            output[offset] = nums[i]

        for i in range(size):
            nums[i] = output[i]


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Key Takeaways
        -------------
        -   Reverse array
        -   Reverse [0:k)
        -   Reverse [k: len(nums))

        Complexity Analysis
        -------------------
        Time Complexity: O(n)
            -   Reverse array: O(n)
            -   Reverse both partitions: O(n)

        Space Complexity: O(1)
            -   no extra space required
        """
        k = k % len(nums)

        # Reverse array
        i, j = 0, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
            i += 1

        # Reverse from [0: k)
        i, j = 0, k - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
            i += 1

        # Reverse from [k: len(nums))
        i, j = k, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
            i += 1
