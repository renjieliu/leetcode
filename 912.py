class Solution:
    def sortArray(self, nums: 'List[int]') -> 'List[int]':
        def swap(arr, a, b):
            t = arr[a]
            arr[a] = arr[b]
            arr[b] = t

        def heapify(arr, pos, n):  # n : last index to be processed
            c1 = 2 * pos + 1
            c2 = c1 + 1
            maxx = pos
            if c1 <= n and arr[c1] > arr[maxx]:
                maxx = c1
            if c2 <= n and arr[c2] > arr[maxx]:
                maxx = c2
            if maxx != pos:
                swap(arr, maxx, pos)
                heapify(arr, maxx, n)

        def build_heap(arr):
            s = (len(arr) - 2) // 2  # (last index-1)//2
            while s > -1:
                heapify(arr, s, len(arr) - 1)
                s -= 1

        def heap_sort(arr):
            build_heap(arr)
            n = len(arr) - 1
            while n > -1:
                swap(arr, 0, n)
                heapify(arr, 0, n - 1)
                n -= 1
            return arr

        return heap_sort(nums)






