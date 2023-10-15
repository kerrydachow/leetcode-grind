class Solution:
    """
    Key Takeaways
    -------------
    -   Brute force solution
    -   Find all differences with a viable indexDifference
    -   Will result in TLE due to test cases

    Complexity Analysis
    -------------------
    Time Complexity: O(n^2)
        - outer loop: O(n)
            -   inner loop: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def findIndices(self, nums: list[int], indexDifference: int, valueDifference: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(indexDifference + i, len(nums)):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]


class Solution:
    """
    Key Takeaways
    -------------
    -   Two pointers
    -   The difference between the min and max must satisfy
        the valueDifference, else no solution is possible
        -   Knowing that, because we have an indexDifference
            constraint that we must satisfy, maintain that
            indexDifference constraint at each iteration
            while keeping track of the current min & max values
    -   Having the min & max with a valid valueDifference:
        -   we can compare the min with the current
            iteration's value
        -   we can also compare the max with the current
            iteration's value
        -   this will guarantee that we're searching for
            the largest difference to find a viable result

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def findIndices(self, nums: list[int], indexDifference: int, valueDifference: int) -> list[int]:
        min_i = 0
        max_i = 0
        for i in range(indexDifference, len(nums)):
            difference = i - indexDifference
            if nums[difference] < nums[min_i]:
                min_i = difference
            if nums[difference] > nums[max_i]:
                max_i = difference
            if abs(nums[min_i] - nums[i]) >= valueDifference:
                return [min_i, i]
            if abs(nums[max_i] - nums[i]) >= valueDifference:
                return [max_i, i]
        return [-1, -1]
