class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        """
        Key Takeaways
        -------------
        -   Binary search
            -   Find the first true
            -   A ship can load between max(weights), and sum(weights)
                on a given day
        -   Write a function to determine the weight is feasible to be
            shipped in less than days # of days

        Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
        [10,  11,  12,  13,  14,  15  ...  55 ]
        ['F', 'F', 'F', 'F', 'F', 'T' ...  'T']
                                   ^

        Complexity Analysis
        -------------------
        Time Complexity: O(nlogm)
            -   sum(): O(n)
            -   max(): O(n)
            -   binary search: O(logm)
                -   where m is in the range sum() - max()

        Space Complexity: O(1)
            -   no extra space required
        """
        def feasible(max_weight):
            res = 1  # start at 1 to include last day
            curr_sum = 0
            for w in weights:
                if curr_sum + w > max_weight:
                    res += 1
                    curr_sum = w
                else:
                    curr_sum += w
            return res <= days

        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


class Solution:
    """
    Key Takeaways
    -------------
    -   Binary search
        -   Find the first false
        -   A ship can load between max(weights), and sum(weights)
            on a given day
    -   Write a function to determine the weight is NOT feasible to be
        shipped in less than days # of days

    Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
    [10,  11,  12,  13,  14,  15  ...  55 ]
    ['T', 'T', 'T', 'T', 'T', 'F' ...  'F']
                               ^

    Complexity Analysis
    -------------------
    Time Complexity: O(nlogm)
        -   sum(): O(n)
        -   max(): O(n)
        -   binary search: O(logm)
            -   where m is in the range sum() - max()

    Space Complexity: O(1)
        -   no extra space required
    """
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def not_feasible(max_weight):
            res = 1  # start at 1 to include last day
            curr_sum = 0
            for w in weights:
                if curr_sum + w > max_weight:
                    res += 1
                    curr_sum = w
                else:
                    curr_sum += w
            return res > days

        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if not_feasible(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo
