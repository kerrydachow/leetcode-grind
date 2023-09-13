class Solution1:
    """
    Key Takeaways
    -------------
    -   Two pointers at beginning and end
    -   Swap until beg == end
    -   while loop

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def reverseString(self, s: list[str]) -> None:
        l, r = 0, len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


class Solution2:
    """
    Key Takeaways
    -------------
    -   Two pointers at beginning and end
    -   Swap until beg == end
    -   for loop with -1-i trick
    -   len(s) // 2 will skip middle element
    -   [0, 1, 2, 3, 4] => 5 // 2 = 2
        -   ignores element 2, does not need to swap
    -   [0, 1, 2, 3] => 4 // 2 = 2

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)

    Space Complexity: O(1)
        -   no extra space required
    """
    def reverseString(self, s: list[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[-1-i] = s[-1-i], s[i]
