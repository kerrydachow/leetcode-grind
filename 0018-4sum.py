class Solution1:
    """
    Key Takeaways
    -------------
    -   Use 3Sum to find 4Sum
    -   Use 2Sum to find 3Sum
    -   Only works for 4Sum
    -   Skip duplicates

    Complexity Analysis
    -------------------
    Time Complexity: O(n^3)
        -   sort: O(nlogn)
        -   2Sum: O(n)
            -   3Sum: O(n)
                -   4Sum: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k, l = j + 1, len(nums) - 1
                while k < l:
                    curr_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if curr_sum > target:
                        l -= 1
                    elif curr_sum < target:
                        k += 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        l -= 1
                        k += 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
        return res


class Solution2:
    """
    Key Takeaways
    -------------
    -   Recursively call for NSum
    -   Base case of 2Sum
    -   Use left and right pointers to slice array
    -   Slice from outer loops of 5, 4, or 3sum
    -   Use array.extend or + to concatenate values to quadruplet

    Complexity Analysis
    -------------------
    Time Complexity: O(n^3)
        -   Recursive outer loop: O(n * k)
            -   where k is the # of loops
        -   2Sum: O(n)
        -   Sort: O(nlogn)

    Space Complexity: O(n * k)
        -   n * k frames on the stack
            -   where k is the # of loops
            -   where n is the # of elements in nums
    """
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        def findNSum(l, r, N, target, quadruplet, res):
            if r-l+1 < N or N < 2:  # handle 1Sum
                return
            if N == 2:
                while l < r:
                    curr_sum = nums[l] + nums[r]
                    if curr_sum > target:
                        r -= 1
                    elif curr_sum < target:
                        l += 1
                    else:
                        res.append(quadruplet + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
            else:
                for i in range(l, r + 1 - N):
                    if i > l and nums[i] == nums[i - 1]:
                        continue
                    else:
                        findNSum(i + 1, r, N-1, target-nums[i], quadruplet + [nums[i]], res)
        nums.sort()
        res = []
        findNSum(0, len(nums)-1, 4, target, [], res)
        return res
