class Solution:
    """
    Key Takeaways
    -------------
    -   Binary search to find which row
    -   Binary search in the row to find exact column

    Complexity Analysis
    -------------------
    Time Complexity: O(log mn)
        -   Binary search to find row: O(log m)
        -   Binary search to find column: O(log n)
        -   O(log m + log n) => O(log(mn))

    Space Complexity: O(1)
        -   no extra space required
    """
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        r_len = len(matrix)  # number of rows
        c_len = len(matrix[0])  # number of columns

        # Binary search to find which row target should belong to
        r_lo, r_hi = 0, r_len - 1
        while r_lo < r_hi:
            r_mid = r_lo + (r_hi - r_lo) // 2
            if matrix[r_mid][0] < target > matrix[r_mid][-1]:
                r_lo = r_mid + 1
            else:
                r_hi = r_mid
        c_lo, c_hi = 0, c_len - 1

        # Binary search to find target in given row
        while c_lo < c_hi:
            c_mid = c_lo + (c_hi - c_lo) // 2
            if matrix[r_lo][c_mid] < target:
                c_lo = c_mid + 1
            else:
                c_hi = c_mid
        return matrix[r_lo][c_lo] == target  # Check if found
