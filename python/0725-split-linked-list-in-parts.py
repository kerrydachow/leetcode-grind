class Solution:
    """
    Key Takeaways
    -------------
    -   Get length
    -   Get the size of each part and append to res array
    -   Split linked list up (iterate through res)
        -   Keep track of prev node
        -   Reassign res[current_index] to curr
        -   Set prev.next to null after each split excluding first split

    Complexity Analysis
    -------------------
    Time Complexity: O(n + k)
        -   get length: O(n)
        -   iterate through res: O(k)
        -   iterate through linked list: O(n)

    Space Complexity: O(k)
        -   temporarily store k sizes in res: O(k)
    """
    def splitListToParts(self, head, k):
        # Get length
        length, curr = 0, head
        while curr:
            curr, length = curr.next, length + 1
        # Determine size of each part
        part_size, part_extra = divmod(length, k)
        res = [part_size + 1] * part_extra + [part_size] * (k - part_extra)
        # Split the linked list
        prev, curr = None, head
        for idx, part in enumerate(res):
            if prev:
                prev.next = None
            res[idx] = curr
            for i in range(part):
                curr, prev = curr.next, curr
        return res
