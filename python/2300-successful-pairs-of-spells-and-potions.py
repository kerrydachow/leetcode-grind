class Solution:
    """
    Key Takeaways
    -------------
    -   Brute force embedded loop approach

    Complexity Analysis
    -------------------
    Time Complexity: O(nm)
        -   first loop: O(n)
            -   embedded loop: O(m)
        -   constraint  1 <= spells[i], potions[i] <= 10^5
            -   will result in TLE for O(nm)

    Space Complexity: O(1)
        -   result array: O(n)
    """
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        res = []
        for spell in spells:  # O(n)
            count = 0
            for potion in potions:  # O(m)
                if spell * potion >= success:
                    count += 1
            res.append(count)
        return res



class Solution:
    """
    Key Takeaways
    -------------
    -   Sort potions
    -   Binary search first false
    -   If lo lands on len(potions), double check to see
        if it is successful

    Complexity Analysis
    -------------------
    Time Complexity: O(mlogm + nlogm)
        -   sort: O(mlogm)
        -   iterate through spells: O(n)
            -   binary search potions: O(logm)

    Space Complexity: O(1)
        -   res: O(n)
    """
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()  # O(mlogm)
        res = []
        for spell in spells:  # O(n)
            # Binary Search
            lo, hi = 0, len(potions) - 1
            while lo < hi:  # O(logm)
                mid = lo + (hi - lo) // 2
                if potions[mid] * spell < success:
                    lo = mid + 1
                else:
                    hi = mid
            if lo == len(potions) - 1 and potions[lo] * spell < success:
                res.append(0)
            else:
                res.append(len(potions) - lo)
        return res
