from collections import defaultdict


class TimeMap:
    """
    Key Takeaways
    -------------
    -   Store values in a dictionary of lists
    -   Store timestamps in a dictionary of lists
    -   Binary search to retrieve the index from timestamps{}
        -   Find last false
    -   Use the index to retrieve value from values{}
    -   Handle uninitialized key-values by returning ""

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   set: O(1)
        -   get: O(logn)
            -   binary search

    Space Complexity: O(n)
        -   where n is the # of values
        -   values_dict: O(n)
        -   timestamps_dict: O(n)
    """
    def __init__(self):
        self.values = defaultdict(list)
        self.timestamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append(value)
        self.timestamps[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if not self.timestamps[key]:
            return ""
        lo, hi = 0, len(self.timestamps[key]) - 1
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if self.timestamps[key][mid] > timestamp:
                hi = mid - 1
            else:
                lo = mid
        return "" if self.timestamps[key][lo] > timestamp else self.values[key][lo]


class TimeMap:
    """
    Key Takeaways
    -------------
    -   Store items in a dictionary where values are
        a list of [value, timestamp]
    -   Binary search to retrieve the index from timestamps{}
        -   Find last false
    -   Handle uninitialized key-values by returning ""

    Complexity Analysis
    -------------------
    Time Complexity: O(logn)
        -   set: O(1)
        -   get: O(logn)
            -   binary search

    Space Complexity: O(n)
        -   total of n elements in initialized data structures
    """
    def __init__(self):
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not self.values[key]:
            return ""
        lo, hi = 0, len(self.values[key]) - 1
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if self.values[key][mid][1] > timestamp:
                hi = mid - 1
            else:
                lo = mid
        return "" if self.values[key][lo][1] > timestamp else self.values[key][lo][0]
