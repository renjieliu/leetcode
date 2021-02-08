class Solution:
    def findRightInterval(self, intervals: 'List[List[int]]') -> 'List[int]':
        arr = []
        for i in range(len(intervals)):
            arr.append([intervals[i][0], i])  # [start, index]
        arr.sort(key=lambda x: x[0])

        def bin(n, arr):  # to search for the smallest start >= end, and return original index
            s = 0
            e = len(arr) - 1
            res = None
            while s <= e:
                mid = (s + e) // 2
                if arr[mid][0] < n:
                    s = mid + 1
                else:
                    res = arr[mid][1]
                    e = mid - 1
            return res if res != None else -1

        output = []
        for i in intervals:
            output.append(bin(i[1], arr))
        return output













