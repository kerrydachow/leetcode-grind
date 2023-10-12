class Iterative:
    """
    Key Takeaways
    -------------
    -   & operation with 1 to check if rightmost bit is 1
    -   Append result of & operation to a count
    -   Shift n with >> operation

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   where n is the # of bits
        -   one pass: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n & 1
            n >>= 1
        return count


class Recursive:
    """
    Key Takeaways
    -------------
    -   Recursively reduce n

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(n)
        -   n frames on the stack: O(n)
    """
    def hammingWeight(self, n: int) -> int:
        if n <= 0:
            return 0
        return (n & 1) + self.hammingWeight(n >> 1)
