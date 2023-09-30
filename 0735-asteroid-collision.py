class Solution:
    """
    Key Takeaways
    -------------
    -   Python's while-else
        -   when break is executed, else does not execute
    -   Stack
    -   Both asteroids destroyed, break
    -   Negative asteroid destroyed, break
    -   If negative asteroid survives, append to stack

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)
        -   while loop will execute at most n times: O(n)

    Space Complexity: O(n)
        -   stack used for output may have N elements
    """
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        res = []
        for a in asteroids:
            # Collision
            while res and res[-1] > 0 and a < 0:
                if abs(a) > res[-1]:
                    res.pop()
                elif abs(a) == res[-1]:
                    res.pop()
                    break
                elif abs(a) < res[-1]:
                    break
            else:
                res.append(a)
        return res


class Solution:
    """
    Key Takeaways
    -------------
    -   Without break statements
    -   Stack
    -   Reassign asteroid to 0 when destroyed

    Complexity Analysis
    -------------------
    Time Complexity: O(n)
        -   one pass: O(n)
        -   while loop executed at most n time: O(n)

    Space Complexity: O(n)
        -   stack used for output may have N elements
    """
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        res = []
        for a in asteroids:
            # Collision
            while res and res[-1] > 0 and a < 0:
                diff = res[-1] + a
                if diff < 0:  # destroyed +asteroid
                    res.pop()
                elif diff > 0:  # -asteroid destroyed
                    a = 0
                else:  # both +-asteroid destroyed
                    a = 0
                    res.pop()
            if a:  # only append if new asteroid exists; > 0
                res.append(a)
        return res
