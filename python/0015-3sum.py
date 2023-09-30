class Solution:
    """
    Key Takeaways
    -------------
    -   Order of output and order of triplets does not matter
    -   Sort the list
    -   Decompose problem into 2sum
    -   Find all 2sum + nums[i] == 0
    -   If nums[i] is > 0, not possible to have sum == 0
    -   Skip all duplicates

    Complexity Analysis
    -------------------
    Time Complexity: O(n^2)
        -   outside loop iterates through nums
        -   inner loop checks for 2sums

    Space Complexity: O(1)
        -   built-in method sort is in-place
    """
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            # not possible to have sum = 0 if nums[i] > 0
            if nums[i] > 0:
                break

            # skip over duplicate nums[i]s
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum > 0:
                    k -= 1
                elif curr_sum < 0:
                    j += 1
                elif curr_sum == 0:
                    res.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        # skip over duplicates
                        j += 1
        return res
