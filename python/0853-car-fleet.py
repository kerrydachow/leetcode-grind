class Solution:
    """
    Key Takeaways
    -------------
    -   Combine position and speed
    -   Sort descending order
    -   Calculate arrival time
        -   (target - position) / speed
    -   If arrival time <= previous car, it will form a fleet
    -   If arrival time > previous car, it will NOT catch up
        to the previous fleet, therefore form a new fleet
    -   Use stack to keep track of fleets

    Complexity Analysis
    -------------------
    Time Complexity: O(nlogn)
        -   sort(): O(nlogn)
        -   zip: O(n)
        -   reverse: O(n)
        -   iterate through fleets: O(n)


    Space Complexity: O(n)
        -   fleets: O(n)
        -   sort: O(n)
        -   stack: O(n)
    """
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []
        fleets = [(p, s) for p, s in zip(position, speed)]
        fleets.sort(reverse=True)

        for p, s in fleets:
            arrival_time = (target - p) / s
            if not stack or stack[-1] < arrival_time:
                stack.append(arrival_time)
        return len(stack)

class Solution:
    """
    Key Takeaways
    -------------
    -   Combine position and speed
    -   Sort descending order
    -   Calculate arrival time
        -   (target - position) / speed
    -   If arrival time <= previous car, it will form a fleet
    -   If arrival time > previous car, it will NOT catch up
        to the previous fleet, therefore form a new fleet

    Complexity Analysis
    -------------------
    Time Complexity: O(nlogn)
        -   sort(): O(nlogn)
        -   zip: O(n)
        -   reverse: O(n)
        -   iterate through fleets: O(n)

    Space Complexity: O(n)
        -   fleets: O(n)
        -   sort: O(n)
    """
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        prev, res = None, 0
        fleets = [(p, s) for p, s in zip(position, speed)]
        fleets.sort(reverse=True)
        for p, s in fleets:
            arrival_time = (target - p) / s
            if not prev or prev < arrival_time:
                prev = arrival_time
                res += 1
        return res
