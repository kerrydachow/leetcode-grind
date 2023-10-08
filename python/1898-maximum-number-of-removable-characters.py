class Solution:
    """
    Key Takeaways
    -------------
    -   Decompose problem
        -   remove characters from s given removable[]
        -   check if removed_s is a subsequence of p
        -   binary search to determine the result
            -   find last true
    -   Binary search with +1 in range to handle discrepancy
        between removable index and the result

    Complexity Analysis
    -------------------
    Time Complexity: O((n+r) * logr)
        - binary search: O((n+r) * logr)
            -   build_s(): O(n+r)
                -   create set: O(r)
                -   iterate through s: O(n)
                -   join(): O(n)
            -   is_subsequence(): O(n)
                -   iterate through s: O(n)
            -   binary search: O(logr)
                -   where r is the length of removable

    Space Complexity: O(n+r)
        -   build[]: O(n)
        -   removable{}: O(r)
    """
    def maximumRemovals(self, s: str, p: str, removable: list[int]) -> int:
        def build_s(num):
            # Build string with removed characters
            # O(n)
            build = []
            set_removable = set(removable[:num])  # O(n)
            for i in range(len(s)):  # O(n)
                if i not in set_removable:
                    build.append(s[i])
            return "".join(build)  # O(n)

        def is_subsequence(a, b):
            # Check if is subsequence
            # O(n)
            j = 0
            for i in range(len(a)):
                if j == len(b):
                    return True
                if a[i] == b[j]:
                    j += 1
            return j == len(b)

        # Binary search with +1 in range to handle
        # discrepancy between removable index and res
        lo, hi = 0, len(removable)
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            removed_s = build_s(mid)
            if is_subsequence(removed_s, p):
                lo = mid
            else:
                hi = mid - 1
        return lo


class Solution:
    """
    Key Takeaways
    -------------
    -   Same solution but optimized by
        -   condensing build_s into is_subsequence
        -   using pointers instead of .join() and an
            array to build the string

    Complexity Analysis
    -------------------
    Time Complexity: O((n+r) * logr)
        -   binary search: O((n+r) * logr)
            -   is_subsequence: O(n+r)
                -   set{}: O(r)
                -   while-loop: O(n)
            -   binary search: O(logr)
                -   where r is the length of removable

    Space Complexity: O(r)
        -   set{}: O(r)
    """
    def maximumRemovals(self, s: str, p: str, removable: list[int]) -> int:
        def is_subsequence(k):
            set_removable = set(removable[:k])  # O(r)
            i = j = 0
            while i < len(s) and j < len(p):  # O(n)
                if i in set_removable:
                    i += 1
                    continue
                if s[i] == p[j]:
                    j += 1
                i += 1
            return j == len(p)

        lo, hi = 0, len(removable)
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if is_subsequence(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
