class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        """
        Key Takeaways
        -------------
        -   Sort the list
        -   Two pointers
        -   Pair the heaviest, with lightest
        -   If a pair can go on a boat, increment i
        -   Always decrement j at each iteration

        Complexity Analysis
        -------------------
        Time Complexity: O(nlogn)
            -   sort: O(nlogn)
            -   2 pointers: O(n)

        Space Complexity: O(1)
            -   no extra space required
        """
        people.sort()
        res = 0
        i, j = 0, len(people) - 1
        while i <= j:
            curr_sum = people[i] + people[j]
            if curr_sum <= limit:
                i += 1
            j -= 1
            res += 1
        return res
