class Solution:
    """
    Key Takeaways
    -------------
    -   Array is sorted
    -   1 indexed
    -   Start one pointer at beginning and one at the end of numbers
    -   If the sum is > target, must decrement end pointer
        -   decrementing end pointer will reduce the sum
    -   If the sum is < target, must increment start pointer
        -   incrementing start pointer will increase the sum

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass

    Space Complexity: O(1)
        -   no extra space required
    """
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            curr_sum = numbers[i] + numbers[j]
            if curr_sum > target:
                j -= 1
            elif curr_sum < target:
                i += 1
            else:
                return [i + 1, j + 1]
        return []
