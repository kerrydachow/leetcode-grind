class Solution:
    """
    Key Takeaways
    -------------
    -   Heap Sort
        -   Heapify the input array
        -   Use the heap property of maintaining the
            max at index 0 to sort the array

    Complexity Analysis
    -------------------
    Time Complexity: O(nlogn)
        -   top-down Heapify: O(logn)
        -   rearranging array: O(n)

    Space Complexity: O(logn)
        -   logn frames on the call stack when heapify: O(logn)
    """
    def sortArray(self, nums: list[int]) -> list[int]:
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and arr[i] < arr[left]:
                largest = left
            if right < n and arr[largest] < arr[right]:
                largest = right
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        def heap_sort(arr):
            n = len(arr)
            for i in range(n // 2, -1, -1):
                heapify(arr, n, i)
            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                heapify(arr, i, 0)

        heap_sort(nums)
        return nums
